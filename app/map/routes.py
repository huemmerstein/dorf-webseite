from flask import Blueprint, render_template

bp = Blueprint('map', __name__, url_prefix='/karte')


@bp.route('/')
def index():
    return render_template('map/index.html')
