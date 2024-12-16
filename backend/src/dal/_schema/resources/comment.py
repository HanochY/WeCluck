from dal._schema.resources._generic import GenericPublic, GenericPrivate, GenericCreate, GenericUpdate 
from pydantic import BaseModel
from uuid import uuid4, UUID

class Models:
    class Public(BaseModel, GenericPublic):
        id: UUID
        uid: UUID
        title: str
        content: str
        topic_id: UUID

    class Private(BaseModel, GenericPrivate):
        id: UUID
        uid: UUID
        title: str
        content: str
        topic_id: UUID

    class Create(BaseModel, GenericCreate):
        uid: UUID
        title: str
        content: str
        topic_id: UUID

    class Update(BaseModel, GenericUpdate):
        uid: UUID | None
        title: str | None
        content: str | None
        topic_id: UUID | None

