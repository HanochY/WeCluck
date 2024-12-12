from dal._schema.repository import BaseRepository
from sqlmodel import Session, select
from sqlalchemy import ColumnExpressionArgument
from dal.sql.forum.tables._common import SQLModelCommon
from typing import Type
from datetime import datetime
from uuid import UUID
class SQLModelRepository(BaseRepository):
    Model: Type[SQLModelCommon]
    
    def __init__(self, Model: Type[SQLModelCommon]):
        self.Model = Model
        
    async def create(self, session: Session, author_id: UUID, **data) -> SQLModelCommon:
        entity = self.Model(**data)
        entity.created_at = datetime.now()
        entity.created_by = author_id
        entity.modified_at = datetime.now()
        entity.modified_by = author_id
        await session.add(entity)
        return entity
        
    async def read(self, 
                   session: Session,
                   filter: ColumnExpressionArgument | None = None, 
                   offset: int | None = None, 
                   limit: int | None = None) -> list[SQLModelCommon | tuple[SQLModelCommon]]:
        statement = select(self.Model)
        if filter:
            statement = statement.where(filter)
        if offset:
            statement = statement.offset(offset)
        if limit: 
            statement = statement.limit(limit)
        entities = await session.execute(statement)
        return entities.scalars().all()
    
    async def update(self, session: Session, author_id: UUID, **new_data) -> SQLModelCommon:
        statement = select(self.Model).where(self.Model.id == id)
        result = await session.exec(statement)
        entity = result.one()
        for attribute, value in new_data.items():
            setattr(entity, attribute, value)
        entity.modified_at = datetime.now()
        entity.modified_by = author_id
        await session.add(entity)

    async def delete(self, session: Session, author_id: UUID, id: UUID) -> SQLModelCommon:
        statement = select(self.Model).where(self.Model.id == id)
        result = await session.exec(statement)
        entity = result.one()
        if entity:
            entity.deleted_at = datetime.now()
            entity.deleted_by = author_id
            entity.is_deleted = True
            await session.add(entity)
        return entity
            
    async def hard_delete(self, session: Session, id: UUID) -> None:
        statement = select(self.Model).where(self.Model.id == id)
        result = await session.exec(statement)
        entity = result.one()
        if entity:
            await session.delete(result)
    