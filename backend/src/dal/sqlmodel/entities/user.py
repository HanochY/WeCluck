from base.entities.user import BaseUser
from metadata import Metadata
from sqlmodel import SQLModel, Field
from typing import Union
    
class User(SQLModel, BaseUser, Metadata, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str