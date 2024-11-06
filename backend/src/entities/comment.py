from pydantic import BaseModel
class CommentBase(BaseModel):
    uid: int
    title: str
    content: str
    topic_id: int
    class Config:
        orm_mode = True

class CommentCreate(CommentBase):
    pass
class CommentRead(BaseModel):
    id: int | None
    uid: int | None
    title: str | None
    content: str | None
    topic_id: int | None
class CommentUpdate(BaseModel):
    uid: int | None
    title: str | None
    content: str | None
    topic_id: int | None
