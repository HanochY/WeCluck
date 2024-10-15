from entities.user import BaseUser
from metadata import Metadata
from sqlmodel import SQLModel, Field

    
class User(SQLModel, BaseUser, Metadata, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    password: str