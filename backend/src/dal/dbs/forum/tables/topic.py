from entities.topic import BaseTopic
from metadata import Metadata
from sqlmodel import SQLModel, Field 
    
class Topic(SQLModel, BaseTopic, Metadata, table=True):
    id: int | None = Field(default=None, primary_key=True)
    uid: int = Field(default=None, foreign_key="user.id")
    content: str