from config.db import database
from datetime import datetime
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
    
    def create(self):
        database.session.add(self)
        database.session.commit()

def read_topics(**kwargs):
    query = database.session.query(Topic)
    if kwargs:
        return query.filter_by(**kwargs).all()
    else:
        return query.all()

def read_topic(**kwargs):
    topics = read_topics(**kwargs)
    return topics[0] if topics else None