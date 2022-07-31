from flask import render_template, abort
from flask_login import login_required


def init_controller(app) -> None:
    @app.route("/", methods=["GET"])
    def home():
        return render_template("index.html")
    