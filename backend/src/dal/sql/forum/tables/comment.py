from dal._schema.resources.comment import Models as CommentModels
from dal.sql.forum.tables._common import SQLModelCommon
from sqlmodel import Field

class Comment(SQLModelCommon, CommentModels.Private, table=True):
    id: int | None = Field(default=None, primary_key=True)
    uid: int = Field(default=None, foreign_key="user.id")
    title: str
    content: str
    topic_id: int = Field(default=None, foreign_key="topic.id")