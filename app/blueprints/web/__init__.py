from app.blueprints.web import home_controller


def init_app(app):
    home_controller.init_controller(app=app)
    