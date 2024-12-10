from dal._schema.resources._validator import validate
from utils.field_injection import inject_fields
from pydantic import BaseModel
from typing import TypedDict

class TypedDicts:
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
        title: str
        content: str
        topic_id: int

    class Update(TypedDict):
        uid: int | None
        title: str | None
        content: str | None
        topic_id: int | None

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