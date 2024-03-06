from config.db import database
from utils.exceptions import *

class User(database.Model):
    _id = database.Column('id', database.Integer, primary_key=True)
    name = database.Column(database.String(32))
    password = database.Column(database.String(32))
 
    def __init__(self, username, password):
       self.name = username
       self.password = password
    
    def to_dict(self):
        data = vars(self)
        data.pop('_sa_instance_state')
        return data

def create_user(username, password):
    new_user = User(username, password)
    database.session.add(new_user)
    database.session.commit()
    
def get_password(username):
    return database.session.query(User.password)\
            .filter_by(name=username).first()[0]

def check_user_exists(username):
    return bool(database.session.query(User._id).
                filter_by(name=username).first())

def get_user_id_by_username(username):
    return database.session.query(User._id).filter_by(name=username).first()[0]

def get_user_by_id(id):
    return database.session.query(User).filter_by(_id=id).first()