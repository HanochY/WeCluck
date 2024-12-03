from dal._schema.entities._validator import validate
from utils.field_injection import inject_fields
from pydantic import BaseModel
from typing import TypedDict

class TypedDict:
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