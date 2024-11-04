from pydantic import BaseModel

class TopicBase(BaseModel):
    uid: int
    title: str
    content: str

class TopicCreate(TopicBase):
    pass
class TopicRead(BaseModel):
    id: int | None
    uid: int | None
    title: str | None
    content: str | None

class TopicUpdate(BaseModel):
    uid: int | None
    title: str | None
    content: str | None