from flask import Flask

from app.ext import config


def minimal_app() -> Flask:
    app = Flask(__name__)
    config.init_app(app=app)
    return app


def create_app() -> Flask:
    app = minimal_app()
    config.load_extensions(app=app)
    return app
