from flask import Blueprint, render_template

from ..models import PinboardPost

bp = Blueprint('pinboard', __name__, url_prefix='/pinboard')


@bp.route('/')
def index():
    posts = PinboardPost.query.order_by(PinboardPost.created_at.desc()).all()
    return render_template('pinboard/index.html', posts=posts)
