from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from qrproject.auth import login_required
from qrproject.db import get_db
from datetime import date, time

bp = Blueprint('qrscan', __name__)

@bp.route('/qrscan')
def qrscan():    
    return render_template('qr/qrscan.html')

@bp.route('/seatregister', methods=('GET', 'POST'))
@login_required
def seat_register():    
    seat = get_db().execute(
        'SELECT eeat_no, occu_id, occu_date, occu_time'
        '  FROM seat WHERE seat_no = ? AND floor = ?',
        (seat_no,floor,)               
    ).fetchone()
    
    #시트 번호가 올바른지 확인    
    if seat is none:
        #에러
        print('시트가 없음')
    else:
        #시트가 비어있는지 확인
        if seat['occu_id'] is not none:
            if seat['occu_id'] is g.user['id']:
                #이미 좌석 등록했음
                print('이미 등록')
            else:
                #시트가 비어있으면 업데이트
                d = date(datetime.now())
                t = time(datetime.now())
                db = get_db()
                db.execute(
                    """UPDATE seat SET occu_id = ?, occu_date = ?, occu_time
                    WHERE seat_no = ? AND floor = ?""",
                    (g.user['id'], d,t, request.form['seat_no'], request.form['floor'])
                )
                db.commit()
                return redirect(url_for('qrscan.qrscan'))