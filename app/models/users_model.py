from typing import Any

from flask_login import UserMixin
from app.ext.flask_sql_alchemy import db
from app.models.model_mixin import ModelMyxin 
from werkzeug.security import generate_password_hash, check_password_hash



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
    
    
    def __repr__(self):
        return f'<User {self.username}>'
    