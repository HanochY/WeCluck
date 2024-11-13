from entities.topic import Topic as TopicGlobal
from dal.models._metadata import Metadata
from sqlmodel import Field 
    
class Topic(TopicGlobal):
    class Table(TopicGlobal.Base, Metadata, table=True):
        id: int | None = Field(default=None, primary_key=True)
        uid: int = Field(default=None, foreign_key="user.id")
        content: str