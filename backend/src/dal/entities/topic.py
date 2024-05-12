from datetime import datetime

from app.db_manager import db_manager

database = db_manager.database

class Topic(database.Model):
    _id = database.Column('id', database.Integer, primary_key=True)
    name = database.Column(database.String(32))
    timestamp = database.Column(
         database.DateTime, nullable=False, default=datetime.now
    )
 
    def __init__(self, name):
        self.name = name
    
    def to_dict(self):
        data = vars(self)
        data.pop('_sa_instance_state')
        return data