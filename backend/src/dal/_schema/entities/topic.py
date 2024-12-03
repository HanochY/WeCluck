from dal._schema.entities._validator import validate
from utils.field_injection import inject_fields
from pydantic import BaseModel
from typing import TypedDict

class TypedDict:
    class Public:
        uid: int
        name: str
        id: int

    class Private:
        uid: int
        name: str
        id: int

    class Create:
        uid: int
        name: str

    class Update:
        uid: int | None
        name: str | None
class Model:
    @inject_fields(TypedDict.Public)
    class Public(BaseModel):
        pass
    @inject_fields(TypedDict.Private)
    class Private(BaseModel):
        pass
    @inject_fields(TypedDict.Create)
    class Create(BaseModel):
        pass
    @inject_fields(TypedDict.Update)
    class Update(BaseModel):
        pass


#validate(...)