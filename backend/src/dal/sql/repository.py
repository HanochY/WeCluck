from dal._schema.repository import BaseRepository
from sqlmodel import Session, select
from sqlalchemy import ColumnExpressionArgument
from dal.sql.forum.models._common import SQLModelCommon
from typing import Type
from datetime import datetime
class SQLModelRepository(BaseRepository):
    Model: Type[SQLModelCommon]
        
    async def create(self, session: Session, author_id: int, **data) -> int:
        """Add <data> to <Table>

        Args:
            Table (SQLModel): Type corresponing with a table in the connected DB.
            **data (kwargs): Data of the new entity.
        Returns:
            id (int): Generated ID of the new entity.
        """
        entity = self.Model(**data)
        entity.created_at = datetime.now()
        entity.created_by = author_id
        entity.modified_at = datetime.now()
        entity.modified_by = author_id
        await session.add(entity)
        return entity.id
        
    async def read(self, 
                   filter: ColumnExpressionArgument, 
                   session: Session,
                   offset: int | None = None, 
                   limit: int | None = None) -> list[SQLModelCommon | tuple[SQLModelCommon]]:
        statement = select(self.Model)
        if filter:
            statement = statement.where(filter)
        if offset:
            statement = statement.offset(offset)
        if limit: 
            statement = statement.limit(limit)
        entities = await session.exec(statement)
        return entities
    
    async def update(self, session: Session, author_id: int, **new_data) -> None:
        statement = select(self.Model).where(self.Model.id == id)
        result = session.exec(statement)
        entity = result.one()
        for attribute, value in new_data.items():
            setattr(entity, attribute, value)
        entity.modified_at = datetime.now()
        entity.modified_by = author_id
        await session.add(entity)

    async def delete(self, session: Session, author_id: int, id: int) -> None:
        statement = select(self.Model).where(self.Model.id == id)
        result = session.exec(statement)
        entity = result.one()
        if entity:
            entity.deleted_at = datetime.now()
            entity.deleted_by = author_id
            entity.is_deleted = True
            await session.add(entity)
            
    async def hard_delete(self, session: Session, id: int) -> None:
        statement = select(self.Model).where(self.Model.id == id)
        result = session.exec(statement)
        entity = result.one()
        if entity:
            await session.delete(result)
    