from dal._schema.entities.base import BaseEntity

class User:
    class Base(BaseEntity.Base):
        name: str
        
    class Public(BaseEntity.Public, Base):
        id: int
        
    class Private(BaseEntity.Private):
        id: int
        password: str
    
    class Create(BaseEntity.Create):
        password: str
        
    class Read(BaseEntity.Read):
        id: int | None
        name: str | None
        password: str | None
    
    class Update(BaseEntity.Update):
        name: str | None
        password: str | None
    