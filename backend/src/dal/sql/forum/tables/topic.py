from dal._schema.entities.topic import Models as TopicModels
from dal.sql.forum.tables._common import SQLModelCommon
from sqlmodel import Field 
class Topic(SQLModelCommon, TopicModels.Private, table=True):
    uid: int = Field(default=None, foreign_key="user.id")
    name: str