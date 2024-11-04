from pydantic import BaseModel
class CommentBase(BaseModel):
    uid: int
    title: str
    content: str
    topic_id: int

class CommentCreate(CommentBase):
    pass
class CommentRead(CommentBase):
    id: int | None
    uid: int | None
    title: str | None
    content: str | None
    topic_id: int | None

class CommentUpdate(CommentBase):
    uid: int | None
    title: str | None
    content: str | None
    topic_id: int | None
