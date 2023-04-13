from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models.user import User

users_app = Blueprint("users_app", __name__, url_prefix='/users', static_folder='../static')


@users_app.route("/", endpoint="list")
def users_list():
    users = User.query.all()
    return render_template("users/list.html", users=users)


@users_app.route("/<int:pk>/", endpoint="details")
def user_details(pk: int):
    user = User.query.filter_by(id=pk).one_or_none()
    if user is None:
        raise NotFound(f"User #{pk} doesn't exist!")
    return render_template("users/details.html", user=user)
