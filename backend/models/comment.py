from config.db import database
from datetime import datetime


class Comment(database.Model):
    _id = database.Column('id', database.Integer, primary_key=True)
    user = database.Column(database.String(32))
    content = database.Column(database.String(32))
    topic_id = database.Column(database.Integer)
    timestamp = database.Column(
        database.DateTime, nullable=False, default=datetime.now
    )
 
    def __init__(self, user, content, topic_id):
        self.user = user
        self.content = content
        self.topic_id = topic_id
 
    def to_dict(self):
        data = vars(self)
        data.pop('_sa_instance_state')
        return data
    
def create_comment(user, content, topic_id):
    new_comment = Comment(user, content, topic_id)
    database.session.add(new_comment)
    database.session.commit()
   
def get_all_comments():
    return Comment.query.all()
    