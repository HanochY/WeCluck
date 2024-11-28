from dal._schema.entities.comment import Comment as CommentGlobal
from dal.sql.forum.models._common import SQLModelCommon
from sqlmodel import SQLModel, Field 
from typing import Type
class CommentTable(SQLModelCommon, table=True):
    id: int | None = Field(default=None, primary_key=True)
    uid: int = Field(default=None, foreign_key="user.id")
    content: str
    topic_id: int = Field(default=None, foreign_key="topic.id")
class Comment(CommentGlobal):
    db_model: Type[SQLModel] = CommentTable