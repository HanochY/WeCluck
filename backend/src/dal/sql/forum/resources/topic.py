from dal.schema.resources.topic import TopicPrivate
from dal.sql.forum.resources._common import SQLModelCommon
from sqlmodel import Field
from uuid import UUID

class DBTopic(SQLModelCommon, TopicPrivate, table=True):
    __tablename__ = "topic"
    uid: UUID = Field(default=None, foreign_key="user.id")
    name: str