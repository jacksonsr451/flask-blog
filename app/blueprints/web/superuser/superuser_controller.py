from flask import flash, redirect, render_template, request

from app.ext.flask_login import login_manager
from app.middlewares.is_superuser_middleware import is_superuser_middleware



def init_controller(app) -> None:
    @app.route("/manager", methods=["GET"])
    @is_superuser_middleware
    def index():
        return render_template("manager/index.html")