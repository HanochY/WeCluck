from dal._schema.entities.base import BaseEntity
class Comment:
    class Base(BaseEntity.Base):
        uid: int
        title: str
        content: str
        topic_id: int
    
    class Public(BaseEntity.Public, Base):
        id: int
        
    class Private(BaseEntity.Private):
        id: int
        
    class Create(BaseEntity.Create, Base):
        pass
    
    class Read(BaseEntity.Read):
        id: int | None
        uid: int | None
        title: str | None
        content: str | None
        topic_id: int | None
        
    class Update(BaseEntity.Update):
        uid: int | None
        title: str | None
        content: str | None
        topic_id: int | None
