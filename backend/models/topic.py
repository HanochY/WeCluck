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
def create_topic(name):
    new_topic = Topic(name)
    database.session.add(new_topic)
    database.session.commit()
    

def get_topic_id_by_name(name):
    return database.session.query(Topic._id)\
            .filter_by(name=name).first()[0]

def check_topic_exists(id):
    return bool(database.session.query(Topic._id).
                filter_by(_id=id).first())

def check_topic_exists_by_name(name):
    return bool(database.session.query(Topic._id).
                filter_by(name=name).first())

def get_all_topics():
    return Topic.query.all()