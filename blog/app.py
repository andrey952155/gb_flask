import os

from flask import Flask
from flask_admin import Admin
from flask_migrate import Migrate

from blog.admin import admin
from blog.api import init_api
from blog.articles_app.views import articles_app
from blog.auth_app.views import auth_app, login_manager
from blog.authors.wies import authors_app
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
    # admin = Admin(app, name='microblog', template_mode='bootstrap3')
    register_blueprints(app)
    admin.init_app(app)
    api = init_api(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(articles_app)
    app.register_blueprint(users_app)
    app.register_blueprint(auth_app)
    app.register_blueprint(index_app)
    app.register_blueprint(authors_app)

