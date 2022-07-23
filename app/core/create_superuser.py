from app.models.users_model import UsersModel
from app.models.users_roles_model import UsersRolesModel
from app.ext.flask_sql_alchemy import db


class CreateSuperuser:
    def __init__(self, username, email, password) -> None:
        self.username = username
        self.email = email
        self.password = password
        self.user_role = UsersRolesModel
        self.user = UsersModel
    
    
    def run(self):
        try:
            self.user.create(username=self.username, email=self.email, password=self.password)
            user = self.user.find_by_username(username=self.username)
            self.user_role.create(user.id, 1)
        except Exception as error:
            db.session.rollback()
            print(error)
        