from datetime import datetime
from app.ext.flask_sql_alchemy import db



class ModelMyxin(object):

    __table_args__ = {'mysql_engine': 'InnoDB'}
    __mapper_args__= {'always_refresh': True}

    id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False)
    
    def __str__(self):
        return self.name

    __mapper_args__ = {
                    'version_id_col': created_at,
                    'version_id_generator': lambda v:datetime.now()
                }