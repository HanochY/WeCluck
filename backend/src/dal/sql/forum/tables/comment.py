from dal._schema.resources.comment import Models as CommentModels
from dal.sql.forum.tables._common import SQLModelCommon
from sqlmodel import Field
from uuid import UUID
class Comment(SQLModelCommon, CommentModels.Private, table=True):
    uid: UUID = Field(default=None, foreign_key="user.id")
    title: str
    content: str
    topic_id: UUID = Field(default=None, foreign_key="topic.id")