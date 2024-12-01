from dal._schema.entities.topic import Topic
from dal.sql.forum.models._common import SQLModelCommon
from sqlmodel import Field 
class TopicTable(SQLModelCommon, Topic.Private, table=True):
    id: int | None = Field(default=None, primary_key=True)
    uid: int = Field(default=None, foreign_key="user.id")
    content: str
