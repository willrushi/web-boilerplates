from flask import Blueprint, render_template

routes = Blueprint("routes", __name__, template_folder="templates")

@routes.route("/")
def index():
    return render_template("index.html")

@routes.route("/<name>")
def params(name):
    return render_template("index.html", name=name)