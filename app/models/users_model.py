from typing import Any
from app.ext.flask_sql_alchemy import db
from app.models.model_mixin import ModelMyxin 



class UsersModel(ModelMyxin, db.Model):
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
        user = UsersModel(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        
        
    @staticmethod
    def find_by_username(username: str):
        return UsersModel.query.filter_by(username=username).first()
    