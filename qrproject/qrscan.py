from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
from werkzeug.exceptions import abort

from qrproject.auth import login_required
from qrproject.db import get_db
from datetime import date, time, datetime

bp = Blueprint('qrscan', __name__)

@bp.route('/qrscan')
def qrscan():    
    print(current_app.config['DATABASE'])
    return render_template('qr/qrscan.html')

@bp.route('/seatregister', methods=('GET', 'POST'))
@login_required
def seat_register():    
    print("hit")
    if request.method == 'POST':
        seat = get_db().execute(
            'SELECT seat_no, occu_id, occu_date, occu_time'
            '  FROM seat WHERE seat_no = ? AND floor = ?',
            (request.form['seat_no'], request.form['floor'],)               
        ).fetchone()

        #시트 번호가 올바른지 확인    
        if seat is None:
            #에러
            error = "시트가 없음"
            flash(error)
        else:
            #시트가 비어있는지 확인
            if seat['occu_id'] is not '' and seat['occu_id'] is not None:
                if seat['occu_id'] is g.user['id']:
                    #본인이 이미 등록했을 떄
                    flash('이미 등록하셨습니다')
                    #return None
                else:
                    #타인이 이미 등록했을 때
                    flash('다른 분이 이미 등록한 좌석입니다')                    
                    #return None 
            else:
                print('true')
                #시트가 비어있으면 업데이트
                # d = date(datetime.now())
                # t = time(datetime.now())
                db = get_db()
                db.execute(
                    """UPDATE seat SET occu_id = ?, occu_date = date('now','localtime'), occu_time = time('now', 'localtime')
                    WHERE seat_no = ? AND floor = ?""",
                    (g.user['id'], request.form['seat_no'], request.form['floor'])
                )
                db.commit()
                flash('등록 완료하였습니다')
                return redirect(url_for('qrscan.qrscan'))
                
    return render_template('qr/qrscan.html')