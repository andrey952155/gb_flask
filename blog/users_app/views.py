from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

users_app = Blueprint("users_app", __name__, url_prefix='/users', static_folder='../static')

USERS = {
    1: "James",
    2: "Brian",
    3: "Peter",
}


@users_app.route("/", endpoint="list")
def users_list():
    return render_template("users/list.html", users=USERS)


@users_app.route("/<int:pk>/", endpoint="details")
def user_details(pk: int):
    try:
        user_name = USERS[pk]
    except KeyError:
        raise NotFound(f"User #{pk} doesn't exist!")
    return render_template('users/details.html', user_id=pk, user_name=user_name)
