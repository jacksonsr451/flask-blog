from flask import render_template, abort

class HomeController:
    def __init__(self, app) -> None:
        @app.route("/")
        def home():
            return render_template("index.html")
