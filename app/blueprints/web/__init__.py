from app.blueprints.web.home_controller import HomeController


def init_app(app):
    HomeController(app=app)
    