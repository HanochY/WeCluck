from entities.user import UserBase
from dal.models.metadata import Metadata
from sqlmodel import Field

    
class User(UserBase, Metadata, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    password: str