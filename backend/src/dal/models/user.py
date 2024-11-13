from entities.user import User as UserGlobal
from dal.models._metadata import Metadata
from sqlmodel import Field

class User(UserGlobal):
    class Table(UserGlobal.Base, Metadata, table=True):
        id: int | None = Field(default=None, primary_key=True)
        name: str
        password: str