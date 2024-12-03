from dal._schema.repository import BaseRepository
from sqlmodel import Session, select
from sqlalchemy import ColumnExpressionArgument
from dal.sql.forum.tables._common import SQLModelCommon
from typing import Type
from datetime import datetime
class SQLModelRepository(BaseRepository):
    Model: Type[SQLModelCommon]
    
    def __init__(self, Model: Type[SQLModelCommon]):
        self.Model = Model
        
    async def create(self, session: Session, author_id: int, **data) -> SQLModelCommon:
        entity = self.Model(**data)
        entity.created_at = datetime.now()
        entity.created_by = author_id
        entity.modified_at = datetime.now()
        entity.modified_by = author_id
        session.add(entity)
        print('aa')
        return entity
        
    async def read(self, 
                   session: Session,
                   filter: ColumnExpressionArgument | None = None, 
                   offset: int | None = None, 
                   limit: int | None = None) -> list[SQLModelCommon | tuple[SQLModelCommon]]:
        statement = select(self.Model)
        print(statement)
        if filter:
            statement = statement.where(filter)
        if offset:
            statement = statement.offset(offset)
        if limit: 
            statement = statement.limit(limit)
        entities = session.exec(statement)
        print(entities)
        return entities
    
    async def update(self, session: Session, author_id: int, **new_data) -> SQLModelCommon:
        statement = select(self.Model).where(self.Model.id == id)
        result = session.exec(statement)
        entity = result.one()
        for attribute, value in new_data.items():
            setattr(entity, attribute, value)
        entity.modified_at = datetime.now()
        entity.modified_by = author_id
        session.add(entity)

    async def delete(self, session: Session, author_id: int, id: int) -> SQLModelCommon:
        statement = select(self.Model).where(self.Model.id == id)
        result = session.exec(statement)
        entity = result.one()
        if entity:
            entity.deleted_at = datetime.now()
            entity.deleted_by = author_id
            entity.is_deleted = True
            session.add(entity)
        return entity
            
    async def hard_delete(self, session: Session, id: int) -> None:
        statement = select(self.Model).where(self.Model.id == id)
        result = session.exec(statement)
        entity = result.one()
        if entity:
            session.delete(result)
    