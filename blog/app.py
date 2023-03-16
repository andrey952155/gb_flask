import os

from flask import Flask
from flask_migrate import Migrate

from blog.articles_app.views import articles_app
from blog.auth_app.views import auth_app, login_manager
from blog.index_app.views import index_app
from blog.models.database import db
from blog.users_app.views import users_app


cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(f"blog.configs.{cfg_name}")
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager.init_app(app)

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(articles_app)
    app.register_blueprint(users_app)
    app.register_blueprint(auth_app)
    app.register_blueprint(index_app)

