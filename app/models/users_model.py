from app.ext.flask_sql_alchemy import db
from app.models.model_mixin import ModelMyxin 



class UsersModel(ModelMyxin, db.Model):
    __tablename__ = 'users'
    
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
