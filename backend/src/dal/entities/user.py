from utils.exceptions import *

from app.db_manager import db_manager

database = db_manager.database

class User(database.Model):
    _id = database.Column('id', database.Integer, primary_key=True)
    name = database.Column(database.String(32))
    password = database.Column(database.String(32))
 
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.password = kwargs.get('password')
    
    def update(self, **kwargs):
        new_name = kwargs.get('name', None)
        new_password = kwargs.get('password', None)
        self.name = new_name if new_name is not None else self.name
        self.password = new_password if new_password is not None else self.password
        
    def to_dict(self):
        data = vars(self)
        data.pop('_sa_instance_state')
        return data