from backend.src.dal.base.repository import BaseRepository
from sqlmodel import Session, SQLModel, select
from sqlalchemy import ColumnExpressionArgument

class SQLModelRepository(BaseRepository):
    def __init__(self, session: Session):
        self.session = session
        
    async def add(self, Entity: SQLModel, **data):
        entity = Entity(**data)
        self.session.add(entity)
        self.session.commit()
        
    async def find(self, 
                   Entity: SQLModel, 
                   *filter: ColumnExpressionArgument[bool], 
                   offset: int | None = None,
                   limit: int | None = None):
        statement = select(Entity)
        if filter:
            statement = statement.where(*filter)
        if offset:
            statement = statement.offset(offset)
        if limit: 
            statement = statement.limit(limit)
        entities = self.session.exec(statement).all()
        return entities
    
    async def edit(self, Entity: SQLModel, id: int, **data):
        statement = select(Entity).where(Entity.id == id)
        result = self.session.exec(statement)
        entity = result.one()
        for attribute, value in data.items():
            setattr(entity, attribute, value)
        self.session.add(entity)
        self.session.commit()

    async def remove(self, 
                     Entity: SQLModel, 
                     id: int):
        statement = select(Entity).where(Entity.id == id)
        result = self.session.exec(statement)
        entity = result.one()
        if entity:
            self.session.delete(result)
            self.session.commit()