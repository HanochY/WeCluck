from dal._schema.entities._validator import validate
from utils.field_injection import inject_fields
from pydantic import BaseModel
from typing import TypedDict

class TypedDict:
    class Public(TypedDict):
        id: int
        uid: int
        title: str
        content: str
        topic_id: int

    class Private(TypedDict):
        id: int
        uid: int
        title: str
        content: str
        topic_id: int

    class Create(TypedDict):
        uid: int
        title: str
        content: str
        topic_id: int

    class Update(TypedDict):
        uid: int | None
        title: str | None
        content: str | None
        topic_id: int | None

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