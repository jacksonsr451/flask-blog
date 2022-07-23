from flask_migrate import Migrate

from app.ext.flask_sql_alchemy import db


migrate = Migrate()


def init_app(app):
    migrate.init_app(app=app, db=db)
    from app import models
