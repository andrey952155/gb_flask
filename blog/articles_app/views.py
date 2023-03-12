from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.users_app.views import USERS

articles_app = Blueprint("articles_app", __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: {'title': 'Заголовок 1', 'text': 'Какой-то текст', 'author': 1},
    2: {'title': 'Заголовок 2', 'text': 'Какой-то текст', 'author': 2},
    3: {'title': 'Заголовок 3', 'text': 'Какой-то текст', 'author': 3},
}


@articles_app.route("/", endpoint="list")
def articles_list():
    return render_template("articles/list.html", articles=ARTICLES)


@articles_app.route("/<int:pk>/", endpoint="details")
def articles_details(pk: int):
    try:
        title = ARTICLES[pk]['title']
        text = ARTICLES[pk]['text']
        author = {'id': ARTICLES[pk]['author'], 'author': USERS[ARTICLES[pk]['author']]}
    except KeyError:
        raise NotFound(f"Articles #{pk} doesn't exist!")
    return render_template('articles/details.html', title=title, text=text, author=author)

