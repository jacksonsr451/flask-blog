from flask import render_template, abort

from app.middlewares.csrf_token_middleware import csrf_token_middleware



def init_controller(app) -> None:
    @app.route("/auth/login")
    def login():
        return render_template("auth/login.html")
    
    
    @app.route('/auth/register', methods=["GET"])
    def register():
        return render_template("auth/register.html")
    
    
    @app.route('/auth/logout', methods=["GET"])
    def logout():
        pass
    
    
    @csrf_token_middleware
    @app.route("/auth/login/validate", methods=["POST"])
    def validate_login():
        return render_template("index.html")
    