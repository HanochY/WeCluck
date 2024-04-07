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
    
def create_comment(uid, content, topic_id):
    new_comment = Comment(uid, content, topic_id)
    database.session.add(new_comment)
    database.session.commit()
   
def get_all_comments():
    return Comment.query.all()
    