from base.entities.comment import BaseComment
from metadata import Metadata
from sqlmodel import SQLModel, Field 
    
class Comment(SQLModel, BaseComment, Metadata, table=True):
    id: int | None = Field(default=None, primary_key=True)
    uid: int = Field(default=None, foreign_key="user.id")
    content: str
    topic_id: int = Field(default=None, foreign_key="topic.id")

