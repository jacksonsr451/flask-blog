from app.blueprints.web import home_controller
from app.blueprints.web.auth import auth_controller



def init_app(app):
    home_controller.init_controller(app=app)
    auth_controller.init_controller(app=app)
    