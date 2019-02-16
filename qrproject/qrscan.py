# coding: utf-8
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
from werkzeug.exceptions import abort

from qrproject.auth import login_required
from qrproject.db import get_db
from datetime import date, time, datetime

bp = Blueprint('qrscan', __name__)

@bp.route('/')
@bp.route('/qrscan')
def qrscan():    
    print(current_app.config['DATABASE'])
    return render_template('qr/qrscan.html')

@bp.route('/seatregister', methods=('GET', 'POST'))
# @login_required
def seat_register():    
    print("hit")    
# 1. QR 접속													
# 	- 스캔												
# 		- 좌석 번호 확인 											
# 			- 좌석번호 맞을 경우 체크할거냐고 물어보기										
# 				- 오케이할 경우									
# 					-미로그인 시 								
# 						- 로그인 화면 리다이렉트							
# 					- 로그인 시								
# 						- 좌석이 존재하는지 확인							
# 							- 좌석이 유효하지 않을 경우 						
# 								- 에러메세지					
# 								- 스캔화면 리다이렉트					
# 							- 좌석이 유효할 경우						
# 								- 좌석이 점유되었는지					
# 									-점유된 사람이 본인인지
# 										- 이 자리 체크아웃?
# 											- 체크아웃		
# 											- 스캔화면 리다이렉트		
# 									- 아니면				
# 										- 다른 사람이 이미 등록한 자리임			
# 								- 비어있으면					
# 									- 로그인 아이디로 체크인				
# 									- 좌석 상태 보여주기				    
    if request.method == 'POST':
        print("!!!")
        seat = get_db().execute(
            'SELECT seat_no, occu_id, occu_date, occu_time'
            '  FROM seat WHERE seat_no = ? AND floor = ?',
            (request.form['seat_no'], request.form['floor'],)               
        ).fetchone()
        print(request.form['seat_no'] + " " + request.form['floor'])
        #시트 번호가 올바른지 확인    
        if seat is None:
            #에러
            error = "시트 번호가 올바르지 않습니다. QR 코드를 확인해주세요."
            flash(error)
            return render_template('qr/qrscan.html')
        else:
            #시트가 비어있는지 확인
            if seat['occu_id'] is not '' and seat['occu_id'] is not None:
                
                # print('seat occu id is ' + str(seat['occu_id']) + ' and user id is ' + str(g.user['id']) )
                
                # if seat['occu_id'] == str(g.user['id']):
                    #본인이 이미 등록했을 떄
                    # flash('이미 등록하셨습니다')
                    # print('이미 등록하셨습니다')
                # else:
                    #타인이 이미 등록했을 때
                    # flash('다른 분이 이미 등록한 좌석입니다')
                    # print('다른 분이 이미 등록한 좌석입니다')
                flash('다른 분이 이미 등록한 좌석입니다')
                print('다른 분이 이미 등록한 좌석입니다')
                return redirect(url_for('qrscan.qrscan',_external=True,_scheme='https',))
            else:
                print('true')
                #시트가 비어있으면 업데이트
                # d = date(datetime.now())
                # t = time(datetime.now())
                db = get_db()
                db.execute(
                    """UPDATE seat SET occu_id = ?, occu_date = date('now','localtime'), occu_time = time('now', 'localtime')
                    WHERE seat_no = ? AND floor = ?""",
                    # (g.user['id'], request.form['seat_no'], request.form['floor'])
                    ("changjin", request.form['seat_no'], request.form['floor'])
                )
                db.commit()
                flash('등록 완료하였습니다')
                print("xxx")
                return redirect(url_for('qrscan.seat_status',_external=True,_scheme='https',))                
    # else:
    #     redirect(url_for('qrscan.qrscan',_external=True,_scheme='https',))                
    
    return render_template('qr/qrscan.html')


@bp.route('/seatregisterjson', methods=['POST'])
# @login_required
def seat_registerjson():
    print("hit")

    if request.method == 'POST':
        print("!!!")
        seat = get_db().execute(
            'SELECT seat_no, occu_id, occu_date, occu_time'
            '  FROM seat WHERE seat_no = ? AND floor = ?',
            (request.json['seat_no'], request.json['floor'],)
        ).fetchone()
        print(request.json['seat_no'] + " " + request.json['floor'])
        # 시트 번호가 올바른지 확인
        if seat is None:
            # 에러
            # error = "시트 번호가 올바르지 않습니다. QR 코드를 확인해주세요."
            error = "check qr code"
            flash(error)
            return render_template('qr/qrscan.html')
        else:
            # 시트가 비어있는지 확인
            if seat['occu_id'] is not '' and seat['occu_id'] is not None:

                # print('seat occu id is ' + str(seat['occu_id']) + ' and user id is ' + str(g.user['id']) )

                # if seat['occu_id'] == str(g.user['id']):
                # 본인이 이미 등록했을 떄
                # flash('이미 등록하셨습니다')
                # print('이미 등록하셨습니다')
                # else:
                # 타인이 이미 등록했을 때
                # flash('다른 분이 이미 등록한 좌석입니다')
                # print('다른 분이 이미 등록한 좌석입니다')
                flash('다른 분이 이미 등록한 좌석입니다')
                print('다른 분이 이미 등록한 좌석입니다')
                return redirect(url_for('qrscan.qrscan', _external=True, _scheme='https', ))
            else:
                print('true')
                # 시트가 비어있으면 업데이트
                # d = date(datetime.now())
                # t = time(datetime.now())
                db = get_db()
                db.execute(
                    """UPDATE seat SET occu_id = ?, occu_date = date('now','localtime'), occu_time = time('now', 'localtime')
                    WHERE seat_no = ? AND floor = ?""",
                    # (g.user['id'], request.form['seat_no'], request.form['floor'])
                    ("changjin", request.json['seat_no'], request.json['floor'])
                )
                db.commit()
                flash('등록 완료하였습니다')
                print("xxx")
                return redirect(url_for('qrscan.seat_status', _external=True, _scheme='https', ))
                # else:
    #     redirect(url_for('qrscan.qrscan',_external=True,_scheme='https',))

    return render_template('qr/qrscan.html')

@bp.route('/seatstatus')
def seat_status():
    seat = get_db().execute(
            "SELECT seat_no, occu_id, occu_date, occu_time, xpos, ypos FROM seat WHERE floor = '6'"
    ).fetchall()
    
    return render_template('qr/seatstatus.html',seat=seat)



