from dal._schema.repository import BaseRepository
from dal._schema.entities._base import BaseEntity
from sqlmodel import Session, SQLModel, select
from sqlalchemy import ColumnExpressionArgument
from typing import Type

class SQLModelRepository(BaseRepository):
    entity: Type[BaseEntity]    
    add_kwargs: dict
    edit_kwargs: dict
    
    def __init__(self, Entity: BaseEntity):
        super.__init__(Entity)
        self.Model = Entity.db_model
        
    async def add(self, session: Session, **add_kwargs) -> int:
        """Add <data> to <Table>

        Args:
            Table (SQLModel): Type corresponing with a table in the connected DB.
            **data (kwargs): Data of the new entity.
        Returns:
            id (int): Generated ID of the new entity.
        """
        entity = self.Model(**add_kwargs)
        await session.add(entity)
        return entity.id
        
    async def find(self, 
                   filter: ColumnExpressionArgument, 
                   session: Session,
                   offset: int | None = None,
                   limit: int | None = None) -> list[SQLModel | tuple[SQLModel]]:
        """Filter <Table> with <filter>, offset by <offset>, limit by <limit>

        Args:
            Table (SQLModel): Type corresponing with a table in the connected DB.
            offset (int | None, optional): SQL adjacent parameter. Defaults to None.
            limit (int | None, optional): SQL adjacent parameter. Defaults to None.

        Returns:
            list[SQLModel]: Query result.
        """
        statement = select(self.Model)
        if filter:
            statement = statement.where(filter)
        if offset:
            statement = statement.offset(offset)
        if limit: 
            statement = statement.limit(limit)
        entities = await session.exec(statement)
        return entities
    
    async def edit(self, session: Session, **edit_kwargs) -> None:
        """Update <id> in <Table> with <data> 

        Args:
            Table (SQLModel): Type corresponing with a table in the connected DB.
            id (int): ID of desired object.
        """
        statement = select(self.Model).where(self.Model.id == id)
        result = session.exec(statement)
        entity = result.one()
        for attribute, value in edit_kwargs.items():
            setattr(entity, attribute, value)
        await session.add(entity)

    async def remove(self,
                     session: Session,
                     id: int) -> None:
        """Remove <id> from <Table>

        Args:
            Table (SQLModel): Type corresponing with a table in the connected DB.
            id (int): ID of desired object.
        """
        statement = select(self.Model).where(self.Model.id == id)
        result = session.exec(statement)
        entity = result.one()
        if entity:
            await session.delete(result)
    
    