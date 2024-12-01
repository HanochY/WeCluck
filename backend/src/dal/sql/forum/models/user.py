from dal._schema.entities.user import User 
from dal.sql.forum.models._common import SQLModelCommon
from sqlmodel import Field

class UserTable(SQLModelCommon, User.Private, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    password: str
