from dal._schema.resources.topic import Models as TopicModels
from dal.sql.forum.tables._common import SQLModelCommon
from sqlmodel import Field
from uuid import UUID

class Topic(SQLModelCommon, TopicModels.Private, table=True):
    uid: UUID = Field(default=None, foreign_key="user.id")
    name: str