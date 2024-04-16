from config.db import database
from utils.exceptions import *

class User(database.Model):
    _id = database.Column('id', database.Integer, primary_key=True)
    name = database.Column(database.String(32))
    password = database.Column(database.String(32))
 
    def __init__(self, name, password):
       self.name = name
       self.password = password
    
    def to_dict(self):
        data = vars(self)
        data.pop('_sa_instance_state')
        return data

    def create(self):
        database.session.add(self)
        database.session.commit()
    

def read_users(**kwargs):
    query = database.session.query(User)
    if kwargs:
        return query.filter_by(**kwargs).all()
    else:
        return query.all()

def read_user(**kwargs):
    users = read_users(**kwargs)
    return users[0] if users else None