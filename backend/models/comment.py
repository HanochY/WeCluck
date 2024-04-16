from config.db import database
from datetime import datetime


class Comment(database.Model):
    _id = database.Column('id', database.Integer, primary_key=True)
    uid = database.Column(database.Integer, database.ForeignKey("user.id"))
    content = database.Column(database.String(32))
    topic_id = database.Column(database.Integer, database.ForeignKey("topic.id"))
    timestamp = database.Column(
        database.DateTime, nullable=False, default=datetime.now
    )
 
    def __init__(self, uid, content, topic_id):
        self.uid = uid
        self.content = content
        self.topic_id = topic_id
 
    def to_dict(self):
        data = vars(self)
        data.pop('_sa_instance_state')
        return data
    
    def create(self):
        database.session.add(self)
        database.session.commit()
    

def read_comments(**kwargs):
    query = database.session.query(Comment)
    if kwargs:
        return query.filter_by(**kwargs).all()
    else:
        return query.all()

def read_comment(**kwargs):
    comments = read_comments(**kwargs)
    return comments[0] if comments else None