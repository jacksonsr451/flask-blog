from email.policy import strict
from app.ext.flask_sql_alchemy import db
from app.models.model_mixin import ModelMyxin 



class RolesModel(ModelMyxin, db.Model):
    __tablename__ = "roles"
    
    role = db.Column(db.String(150), unique=True, nullable=False)
    
    
    def __init__(self, id = None, role: str = "") -> None:
        self.id = None
        self.role = role 
        
    
    @staticmethod
    def create(id = None, role: str = ""):
        if id is not None:
            new_user = RolesModel(id, role)
        else:
            new_user = RolesModel(role)
        db.session.add(new_user)
        db.session.commit()