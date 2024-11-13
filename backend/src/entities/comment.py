from pydantic import BaseModel
class Comment:
    class Base(BaseModel):
        uid: int
        title: str
        content: str
        topic_id: int

    class Create(Base):
        pass
    
    class Read(BaseModel):
        id: int | None
        uid: int | None
        title: str | None
        content: str | None
        topic_id: int | None
        
    class Update(BaseModel):
        uid: int | None
        title: str | None
        content: str | None
        topic_id: int | None
