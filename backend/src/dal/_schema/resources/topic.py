from dal._schema.resources._generic import GenericPublic, GenericPrivate, GenericCreate, GenericUpdate
from utils.field_injection import inject_fields
from pydantic import BaseModel
from typing import TypedDict
from uuid import uuid4, UUID

class Models:
    class Public(BaseModel, GenericPublic):
        uid: UUID
        name: str
        id: UUID

    class Private(BaseModel, GenericPrivate):
        uid: UUID
        name: str
        id: UUID

    class Create(BaseModel, GenericCreate):
        uid: UUID
        name: str

    class Update(BaseModel, GenericUpdate):
        uid: UUID | None
        name: str | None
