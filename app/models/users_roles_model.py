from app.ext.flask_sql_alchemy import db
from app.models.model_mixin import ModelMyxin


class UsersRolesModel(ModelMyxin, db.Model):
    __tablename__ = "user_role"
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    
    def __init__(self, user_id, role_id) -> None:
        self.user_id = user_id
        self.role_id = role_id
        
        
    @staticmethod
    def create(user_id, role_id):
        user_role = UsersRolesModel(user_id=user_id, role_id=role_id)
        db.session.add(user_role)
        db.session.commit()
    