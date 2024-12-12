from dal._schema.resources._validator import validate
from utils.field_injection import inject_fields
from pydantic import BaseModel
from typing import TypedDict
from uuid import uuid4, UUID

class TypedDicts:
    class Public(TypedDict):
        id: UUID
        uid: UUID
        title: str
        content: str
        topic_id: UUID

    class Private(TypedDict):
        id: UUID
        uid: UUID
        title: str
        content: str
        topic_id: UUID

    class Create(TypedDict):
        title: str
        content: str
        topic_id: UUID

    class Update(TypedDict):
        uid: UUID | None
        title: str | None
        content: str | None
        topic_id: UUID | None

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