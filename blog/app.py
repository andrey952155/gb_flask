from flask import Flask

from blog.articles_app.views import articles_app
from blog.auth_app.views import auth_app, login_manager
from blog.index_app.views import index_app
from blog.models.database import db
from blog.users_app.views import users_app


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "abcdefg123456"

    db.init_app(app)
    login_manager.init_app(app)

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(articles_app)
    app.register_blueprint(users_app)
    app.register_blueprint(auth_app)
    app.register_blueprint(index_app)

