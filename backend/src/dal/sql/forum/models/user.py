from dal._schema.entities.user import User as UserGlobal
from dal.sql.forum.models._common import SQLModelCommon
from sqlmodel import SQLModel, Field
from typing import Type
class UserTable(SQLModelCommon, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    password: str
class User(UserGlobal):
    db_model: Type[SQLModel] = UserTable