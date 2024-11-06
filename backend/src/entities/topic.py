from pydantic import BaseModel

class TopicBase(BaseModel):
    uid: int
    name: str
    class Config:
        orm_mode = True

class TopicCreate(TopicBase):
    pass
class TopicRead(BaseModel):
    id: int | None
    uid: int | None
    name: str | None

class TopicUpdate(BaseModel):
    uid: int | None
    name: str | None
