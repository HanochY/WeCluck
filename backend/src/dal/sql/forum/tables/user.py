from dal._schema.resources.user import Models as UserModels
from dal.sql.forum.tables._common import SQLModelCommon
from sqlmodel import Field
class User(SQLModelCommon, UserModels.Private, table=True):
    name: str
    password: str
