from entities.topic import TopicBase
from dal.models.metadata import Metadata
from sqlmodel import Field 
    
class Topic(TopicBase, Metadata, table=True):
    id: int | None = Field(default=None, primary_key=True)
    uid: int = Field(default=None, foreign_key="user.id")
    content: str