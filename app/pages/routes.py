from flask import Blueprint, render_template

from ..models import Page

bp = Blueprint('pages', __name__)


@bp.route('/seite/<slug>')
def page(slug):
    page_obj = Page.query.filter_by(slug=slug).first_or_404()
    return render_template('pages/page.html', page=page_obj)


@bp.route('/impressum')
def impressum():
    return render_template('pages/impressum.html')


@bp.route('/datenschutz')
def datenschutz():
    return render_template('pages/datenschutz.html')


@bp.route('/geschichte')
def geschichte():
    page_obj = Page.query.filter_by(slug='geschichte').first()
    return render_template('pages/geschichte.html', page=page_obj)
