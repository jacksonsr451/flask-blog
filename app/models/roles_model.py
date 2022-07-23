from app.ext.flask_sql_alchemy import db
from app.models.model_mixin import ModelMyxin 



class RolesModel(ModelMyxin, db.Model):
    __tablename__ = "roles"
    
    role = db.Column(db.String(150), unique=True, nullable=False)