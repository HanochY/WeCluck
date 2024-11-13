from dal._schema.entities.base import BaseEntity

class Topic:
    class Base(BaseEntity.Base):
        uid: int
        name: str
    
    class Public(BaseEntity.Public, Base):
        id: int
        
    class Private(BaseEntity.Private):
        id: int
    
    class Create(BaseEntity.Create, Base):
        pass
    
    class Read(BaseEntity.Read):
        id: int | None
        uid: int | None
        name: str | None
    
    class Update(BaseEntity.Update):
        uid: int | None
        name: str | None
    