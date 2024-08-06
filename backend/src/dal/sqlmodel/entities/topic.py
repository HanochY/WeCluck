from dal.sqlalchemy.entities.base import BaseEntity
from datetime import datetime
from backend.src.dbs.db_manager import db_manager

database = db_manager.database

class TopicEntity(BaseEntity, db_manager.database.Model):
    id = database.Column('id', database.Integer, primary_key=True)
    name = database.Column(database.String(32))
    timestamp = database.Column(
         database.DateTime, nullable=False, default=datetime.now
    )

from dal.sqlalchemy.entities.base import BaseEntity
from datetime import datetime
from sqlmodel import Field

class CommentEntity(BaseEntity, table=True):
    id: int | None = Field(default=None, primary_key=True)
    uid: int = Field(default=None, foreign_key="user.id")
    name: str
    topic_id: int = Field(default=None, foreign_key="topic.id")
    timestamp: datetime = Field(default=datetime.now)