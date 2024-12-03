from dal._schema.entities._validator import validate
from utils.field_injection import inject_fields
from pydantic import BaseModel
from typing import TypedDict

class TypedDicts:
    class Public:
        id: int
        name: str

    class Private:
        id: int
        name: str
        password: str

    class Create:
        name: str
        password: str

    class Update:
        name: str | None
        password: str | None
        
class Models:
    @inject_fields(TypedDicts.Public)
    class Public(BaseModel):
        pass
    @inject_fields(TypedDicts.Private)
    class Private(BaseModel):
        pass
    @inject_fields(TypedDicts.Create)
    class Create(BaseModel):
        pass
    @inject_fields(TypedDicts.Update)
    class Update(BaseModel):
        pass


#validate(...)