from dal._schema.entities.comment import Comment
from dal.sql.forum.models._common import SQLModelCommon
from sqlmodel import Field

class CommentTable(SQLModelCommon, Comment.Private, table=True):
    id: int | None = Field(default=None, primary_key=True)
    uid: int = Field(default=None, foreign_key="user.id")
    title: str
    content: str
    topic_id: int = Field(default=None, foreign_key="topic.id")