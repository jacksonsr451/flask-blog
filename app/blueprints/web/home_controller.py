from flask import render_template, abort


def init_controller(app) -> None:
    @app.route("/", methods=["GET"])
    def home():
        return render_template("index.html")
    