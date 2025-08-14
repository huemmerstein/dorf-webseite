from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    from .news.routes import bp as news_bp
    from .events.routes import bp as events_bp
    from .flurnamen.routes import bp as flurnamen_bp
    from .pinboard.routes import bp as pinboard_bp
    from .pages.routes import bp as pages_bp
    from .map.routes import bp as map_bp

    app.register_blueprint(news_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(flurnamen_bp)
    app.register_blueprint(pinboard_bp)
    app.register_blueprint(pages_bp)
    app.register_blueprint(map_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
