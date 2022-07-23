from app.models.roles_model import RolesModel


class InitRoles:
    def __init__(self) -> None:
        self.role = RolesModel    
    
    
    def run(self):
        self.role.create(id=1, role="superuser")
        self.role.create(id=2, role="admin")
        self.role.create(id=3, role="user")    
        