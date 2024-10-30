from repositories.base import BaseRepository
from sqlmodel import Session, SQLModel, select
from sqlalchemy import ColumnExpressionArgument
from fastapi_filter.contrib.sqlalchemy import Filter

class SQLModelRepository(BaseRepository):
    def __init__(self, Model: SQLModel):
        """New Repository.

        Args:
            session (Session): DB Session. This enables concurrency.
        """
        self.Model = Model
    
    async def add(self, session: Session, **data) -> int:
        """Add <data> to <Table>

        Args:
            Table (SQLModel): Type corresponing with a table in the connected DB.
            **data (kwargs): Data of the new entity.
        Returns:
            id (int): Generated ID of the new entity.
        """
        entity = self.Model(**data)
        session.add(entity)
        return entity.id
        
    async def find(self, 
                   session: Session,
                   filter: Filter, 
                   offset: int | None = None,
                   limit: int | None = None) -> list[SQLModel]:
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
            statement = filter.filter(statement)
        if offset:
            statement = statement.offset(offset)
        if limit: 
            statement = statement.limit(limit)
        entities = session.exec(statement).all()
        return entities
    
    async def edit(self, session: Session, id: int, **data) -> None:
        """Update <id> in <Table> with <data> 

        Args:
            Table (SQLModel): Type corresponing with a table in the connected DB.
            id (int): ID of desired object.
        """
        statement = select(self.Model).where(self.Model.id == id)
        result = session.exec(statement)
        entity = result.one()
        for attribute, value in data.items():
            setattr(entity, attribute, value)
        session.add(entity)

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
            session.delete(result)
    
    