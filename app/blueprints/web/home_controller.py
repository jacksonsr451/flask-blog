from flask import render_template, abort

from app.middlewares.csrf_token_middleware import csrf_token_middleware


def init_controller(app) -> None:
    @app.route("/", methods=["GET"])
    def home():
        return render_template("index.html")
    
    
    @csrf_token_middleware
    @app.route("/auth/login", methods=["POST"])
    def login():
        return render_template("index.html")
