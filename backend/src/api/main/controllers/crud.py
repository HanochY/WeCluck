from utils.exceptions import *
from dal.sql.repository import SQLModelRepository, SQLModel
from dal.sql.forum.db_manager import get_db_session
from fastapi import HTTPException, status

class Controller:
    def __init__(self, Model: SQLModel):
        self.repository = SQLModelRepository(Model=Model)
    
    async def create(self, object):
        try:
            with await get_db_session() as session:
                id = await self.repository.add(**object, session=session)
        except TypeError:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Item not found")
        return id or None
    
    async def read(self, id):
        try:
            with await get_db_session() as session:
                id = await self.repository.find(id==id, session=session)
        except TypeError:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Item not found")
        return id or None
    
    
    
    async def update(self, id, object):
        with await get_db_session() as session:
            user = await self.repository.edit(**object, id=id, session=session)
        return user or None
    
    async def delete(self, id):
        with await get_db_session() as session:
            user = await self.repository.remove(id=id, session=session)
        return user or None
    