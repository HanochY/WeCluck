from pydantic import BaseModel

class Topic:
    class Base(BaseModel):
        uid: int
        name: str
        class Config:
            orm_mode = True
    
    class Create(Base):
        pass
    class Read(BaseModel):
        id: int | None
        uid: int | None
        name: str | None
    
    class Update(BaseModel):
        uid: int | None
        name: str | None
    