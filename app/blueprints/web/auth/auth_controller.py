from flask import flash, redirect, render_template, request
from flask_login import login_required, login_user, logout_user

from app.middlewares.csrf_token_middleware import csrf_token_middleware
from app.ext.flask_login import login_manager
from app.models.users_model import UsersModel
from app.models.users_roles_model import UsersRolesModel



def init_controller(app) -> None:
    @app.route("/auth/login")
    def login():
        return render_template("auth/login.html")
    
    
    @csrf_token_middleware
    @app.route("/auth/login/validate", methods=["POST"])
    def validate_login():
        data = request.values
        user = UsersModel.login(username=data["username"], password=data["password"])
        if user is not None:
            login_user(user=user)
            flash("Usuário logado", "success")
            return redirect("/")
        flash("Erro de login", "error")
        return redirect("/auth/login")        
    
    
    @app.route('/auth/register', methods=["GET"])
    def register():
        return render_template("auth/register.html")
    
    
    @app.route('/auth/register/validate', methods=["POST"])
    def register_validate():
        data =  request.values
        try:
            UsersModel.create(username=data["username"], password=data["password"], email=data["email"])
            user = UsersModel.find_by_username(username=data["username"])
            UsersRolesModel.create(user_id=user.id, role_id=3)
            return redirect('/auth/login')
        except:
            # TODO: Implementing rollback data
            return redirect('/auth/register')
    
    
    @app.route('/auth/logout', methods=["GET"])
    @login_required
    def logout():
        logout_user()
        return redirect("/auth/login")
    
    
    @login_manager.user_loader
    def load_user(user_id):
        return UsersModel.find_user_by_id(user_id=user_id)
    