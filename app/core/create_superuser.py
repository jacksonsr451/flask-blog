from app.models.roles_model import RolesModel


class CreateSuperuser:
    def __init__(self, username, email, password) -> None:
        self.username = username
        self.email = email
        self.password = password
        self.role = RolesModel
        
    
    
    def run(self):
        self.role.create(id=1, role="superuser")    
    
        