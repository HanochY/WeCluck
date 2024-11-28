from dal._schema.entities._base import BaseEntity
from pydantic import BaseModel

class Common(BaseModel):
    uid: int | None
    title: str | None
    content: str | None
    topic_id: int | None

class Public(Common):
    id: int
    uid: int
    title: str
    content: str
    topic_id: int
    

class Create(Common):
    uid: int
    title: str
    content: str
    topic_id: int

class Read(Common):
    id: int | None
    
    
class Update(Common):
    pass

class Comment(BaseEntity):
    _base = Common
    private = Public
    public = Public
    create = Create
    update = Update