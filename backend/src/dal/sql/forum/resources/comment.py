from dal.schema.resources.comment import CommentPrivate
from dal.sql.forum.resources._common import SQLModelCommon
from sqlmodel import Field
from uuid import UUID
class DBComment(SQLModelCommon, CommentPrivate, table=True):
    __tablename__ = "comment"
    uid: UUID = Field(default=None, foreign_key="user.id")
    title: str
    content: str
    topic_id: UUID = Field(default=None, foreign_key="topic.id")