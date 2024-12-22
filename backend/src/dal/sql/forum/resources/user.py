from dal.schema.resources.user import UserPrivate
from dal.sql.forum.resources._common import SQLModelCommon
from sqlmodel import Field
class DBUser(SQLModelCommon, UserPrivate, table=True):
    __tablename__ = "user"
    name: str
    password: str
