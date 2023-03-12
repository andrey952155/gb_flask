from flask import Flask, Blueprint

from blog.articles_app.views import articles_app
from blog.users_app.views import users_app


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(articles_app)
    app.register_blueprint(users_app)

