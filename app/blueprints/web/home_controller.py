from flask import render_template, abort

from app.middlewares.superuser_middleware import csrf_token_middleware


def init_controller(app) -> None:
    @app.route("/")
    @csrf_token_middleware
    def home():
        return render_template("index.html")
