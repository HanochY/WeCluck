from dal._schema.entities.topic import Topic as TopicGlobal
from dal.sql.forum.models._common import SQLModelCommon
from sqlmodel import SQLModel, Field 
from typing import Type
class TopicTable(SQLModelCommon, table=True):
    id: int | None = Field(default=None, primary_key=True)
    uid: int = Field(default=None, foreign_key="user.id")
    content: str
    
class Topic(TopicGlobal):
    db_model: Type[SQLModel] = TopicTable
