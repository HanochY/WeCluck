from dal._schema.entities._base import BaseEntity
from pydantic import BaseModel
from typing import Type

class Common(BaseModel):
    name: str | None
    
class Public(Common):
    id: int
    name: str
    
class Private(Common):
    id: int
    name: str
    password: str

class Create(Common):
    name: str
    password: str
    
class Read(Common):
    id: int | None
    password: str | None

class Update(Common):
    password: str | None

class User(BaseEntity):
    _base = Common
    private = Private
    public = Public
    create: Type = Create
    update = Update