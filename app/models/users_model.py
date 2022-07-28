from array import array
from typing import Any

from flask_login import UserMixin, current_user
from app.ext.flask_sql_alchemy import db
from app.models.model_mixin import ModelMyxin 
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.roles_model import RolesModel

from app.models.users_roles_model import UsersRolesModel



class UsersModel(ModelMyxin, db.Model, UserMixin):
    __tablename__ = 'users'
    
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    
    
    def __init__(self, username: str, email: str, password: str) -> None:
        self.username = username
        self.email = email
        self.password = password
        
    
    @staticmethod
    def create(username: str, email: str, password: str) -> None:
        user = UsersModel(username=username, password=generate_password_hash(password).__str__(), email=email)
        db.session.add(user)
        db.session.commit()
        
        
    @staticmethod
    def find_by_username(username: str):
        return UsersModel.query.filter_by(username=username).first()
    
    
    @staticmethod
    def login(username: str, password):
        user = UsersModel.query.filter_by(username=username).first()
        if check_password_hash(user.password, password):
            return user
        return None
    
    
    @staticmethod
    def find_user_by_id(user_id):
        return UsersModel.query.get(user_id)
    
    
    @staticmethod
    def roles():
        roles: list = list()
        users_roles = UsersRolesModel.query.filter_by(user_id=current_user.id)
        for role in users_roles:
            current_role = RolesModel.query.filter_by(id=role.role_id).first()
            roles.append({
                "user_id": role.user_id,
                "role": current_role.role
            })
        return roles
    
    
    def __repr__(self):
        return f'<User {self.username}>'
    