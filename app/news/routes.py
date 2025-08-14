from flask import Blueprint, render_template, abort, Response
from feedgen.feed import FeedGenerator

from ..models import News
from .. import db

bp = Blueprint('news', __name__, url_prefix='/news')


@bp.route('/')
def index():
    posts = News.query.order_by(News.created_at.desc()).all()
    return render_template('news/index.html', posts=posts)


@bp.route('/<int:news_id>')
def detail(news_id):
    post = News.query.get_or_404(news_id)
    return render_template('news/detail.html', post=post)


@bp.route('/rss')
def rss():
    fg = FeedGenerator()
    fg.title('News')
    fg.link(href='')
    fg.description('Neuigkeiten')
    for post in News.query.order_by(News.created_at.desc()).limit(20):
        fe = fg.add_entry()
        fe.title(post.title)
        fe.link(href=f"/news/{post.id}")
        fe.description(post.body)
        fe.pubDate(post.created_at)
    rssfeed = fg.rss_str(pretty=True)
    return Response(rssfeed, mimetype='application/rss+xml')
