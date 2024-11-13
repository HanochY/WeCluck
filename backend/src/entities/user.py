from pydantic import BaseModel

class User:
    class Base(BaseModel):
        name: str
        class Config:
            orm_mode = True
        
    class Public(Base):
        id: int
        
    class Private(Public):
        password: str
    
    class Create(Base):
        password: str
        
    class Read(BaseModel):
        id: int | None
        name: str | None
        password: str | None
    
    class Update(BaseModel):
        name: str | None
        password: str | None
    