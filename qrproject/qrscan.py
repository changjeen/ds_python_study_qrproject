from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from qrproject.auth import login_required
from qrproject.db import get_db

bp = Blueprint('qrscan', __name__)

@bp.route('/qrscan')
def qrscan():    
    return render_template('qr/qrscan.html')
