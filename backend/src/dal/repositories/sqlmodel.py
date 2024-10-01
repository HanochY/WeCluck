from repositories.base import BaseRepository
from sqlmodel import Session, SQLModel, select
from sqlalchemy import ColumnExpressionArgument

class SQLModelRepository(BaseRepository):
    def __init__(self, session: Session):
        """New Repository.

        Args:
            session (Session): DB Session. This enables concurrency.
        """
        self.session = session
    
    async def commit(self):
        self.session.commit()
    
    async def add(self, Table: SQLModel, **data) -> None:
        """Add <data> to <Table>

        Args:
            Table (SQLModel): Type corresponing with a table in the connected DB.
            **data (kwargs): Data of the new entity.
        """
        entity = Table(**data)
        self.session.add(entity)
        
    async def find(self, 
                   Table: SQLModel, 
                   *filter: ColumnExpressionArgument[bool], 
                   offset: int | None = None,
                   limit: int | None = None) -> list[SQLModel]:
        """Filter <Table> with <filter>, offset by <offset>, limit by <limit>

        Args:
            Table (SQLModel): Type corresponing with a table in the connected DB.
            *filter (*ColumnExpressionArgument): SQLModel bool-like object.
            e.g. Building.floor <= 3, Building.color == 'white', ...
            offset (int | None, optional): SQL adjacent parameter. Defaults to None.
            limit (int | None, optional): SQL adjacent parameter. Defaults to None.

        Returns:
            list[SQLModel]: Query result.
        """
        statement = select(Table)
        if filter:
            statement = statement.where(*filter)
        if offset:
            statement = statement.offset(offset)
        if limit: 
            statement = statement.limit(limit)
        entities = self.session.exec(statement).all()
        return entities
    
    async def edit(self, Table: SQLModel, id: int, **data) -> None:
        """Update <id> in <Table> with <data> 

        Args:
            Table (SQLModel): Type corresponing with a table in the connected DB.
            id (int): ID of desired object.
        """
        statement = select(Table).where(Table.id == id)
        result = self.session.exec(statement)
        entity = result.one()
        for attribute, value in data.items():
            setattr(entity, attribute, value)
        self.session.add(entity)

    async def remove(self, 
                     Table: SQLModel, 
                     id: int) -> None:
        """Remove <id> from <Table>

        Args:
            Table (SQLModel): Type corresponing with a table in the connected DB.
            id (int): ID of desired object.
        """
        statement = select(Table).where(Table.id == id)
        result = self.session.exec(statement)
        entity = result.one()
        if entity:
            self.session.delete(result)
    
    