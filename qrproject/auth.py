import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from qrproject.db import get_db

import re


bp = Blueprint('auth', __name__, url_prefix='/auth')


def verifyemail(email):        
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

    if match == None:
        return False
    else: 
        return True

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']        
        password_re = request.form['password-re']      
        email = request.form['email']
        rnk = request.form['rnk']
        phone_no = request.form['phone_no']
        user_type = '2'
        
        db = get_db()
        error = None
        
        if not verifyemail(email):
            error = '이메일이 올바르지 않습니다.'           
        elif password != password_re:
            error = '동일한 비밀번호를 입력해 주세요.'           
        elif username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE email = ?', (email,)
        ).fetchone() is not None:
            #error = '이미 가입되어있는 이메일 주소입니다.'.format(username)
            error = '이미 가입되어있는 이메일 주소입니다.'
            
        if error is None:
            db.execute(
                'INSERT INTO user (username, password,user_type,rnk,phone_no) VALUES (?, ?, ?, ?, ?)',
                (username, generate_password_hash(password), user_type, rnk, phone_no)
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if g.user is not None:
        
        return redirect(url_for('qrscan.qrscan',_external=True,_scheme='https',))                
    else:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            db = get_db()
            error = None
            user = db.execute(
                'SELECT * FROM user WHERE email = ?', (email,)
            ).fetchone()

            if user is None:
                error = '이메일/비밀번호가 올바르지 않습니다.'
            elif not check_password_hash(user['password'], password):
                error = '이메일/비밀번호가 올바르지 않습니다.'

            if error is None:
                session.clear()
                session['user_id'] = user['id']
                return redirect(url_for('qrscan.qrscan',_external=True,_scheme='https',))            

            flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
        
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login',_external=True,_scheme='https',))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash('먼저 로그인이 필요합니다.')
            return redirect(url_for('auth.login',_external=True,_scheme='https',))

        return view(**kwargs)

    return wrapped_view