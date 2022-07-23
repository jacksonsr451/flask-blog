from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app, **config):
    db.init_app(app=app, **config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
