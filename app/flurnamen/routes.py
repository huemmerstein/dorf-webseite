from flask import Blueprint, render_template

from ..models import Flurname

bp = Blueprint('flurnamen', __name__, url_prefix='/flurnamen')


@bp.route('/')
def index():
    items = Flurname.query.order_by(Flurname.name).all()
    return render_template('flurnamen/index.html', items=items)
