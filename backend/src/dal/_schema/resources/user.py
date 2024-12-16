from dal._schema.resources._generic import GenericPublic, GenericPrivate, GenericCreate, GenericUpdate
from utils.field_injection import inject_fields
from pydantic import BaseModel
from typing import TypedDict
from uuid import uuid4, UUID

class Models:
    class Public(BaseModel, GenericPublic):
        id: UUID
        name: str

    class Private(BaseModel, GenericPrivate):
        id: UUID
        name: str
        password: str

    class Create(BaseModel, GenericCreate):
        name: str
        password: str

    class Update(BaseModel, GenericUpdate):
        name: str | None
        password: str | None
