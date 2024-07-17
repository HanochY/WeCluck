from dal.sqlalchemy.entities.base import BaseEntity
from datetime import datetime
from app.db_manager import db_manager
from dal.sqlalchemy.entities.topic import TopicEntity
from dal.sqlalchemy.entities.user import UserEntity

database = db_manager.database

class CommentEntity(BaseEntity, db_manager.database.Model):
    id = database.Column('id', database.Integer, primary_key=True)
    uid = database.Column(database.Integer, database.ForeignKey(UserEntity.id))
    content = database.Column(database.String(32))
    topic_id = database.Column(database.Integer, database.ForeignKey(TopicEntity.id))
    timestamp = database.Column(
        database.DateTime, nullable=False, default=datetime.now
    )