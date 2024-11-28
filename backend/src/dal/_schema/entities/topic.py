from dal._schema.entities._base import BaseEntity
from pydantic import BaseModel
class Common(BaseModel):
    uid: int | None
    name: str | None

class Public(Common):
    uid: int
    name: str
    id: int

class Create(Common):
    uid: int
    name: str

class Read(Common):
    id: int | None

class Update(Common):
    pass

class Topic(BaseEntity):
    _base = Common
    private = Public
    public = Public
    create = Create
    update = Update