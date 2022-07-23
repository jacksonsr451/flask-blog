from app.ext.flask_sql_alchemy import db
from app.models.model_mixin import ModelMyxin


class UsersRolesModel(ModelMyxin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    user = db.relationship('Roles', backref='roles', lazy='dynamic')
    role = db.relationship('Users', backref='user', lazy='dynamic')
    