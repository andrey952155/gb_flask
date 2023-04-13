from flask import render_template, Blueprint

index_app = Blueprint("index_app", __name__, static_folder='../static')


@index_app.route("/", endpoint="index")
def articles_list():
    return render_template("index/index.html")
