from dal.sqlalchemy.entities.base import BaseEntity
from datetime import datetime
from sqlmodel import Field

class CommentEntity(BaseEntity, table=True):
    id: int | None = Field(default=None, primary_key=True)
    uid: int = Field(default=None, foreign_key="user.id")
    content: str
    topic_id: int = Field(default=None, foreign_key="topic.id")
    timestamp: datetime = Field(default=datetime.now)