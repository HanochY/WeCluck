from utils.exceptions import *
from dal.sql.repository import SQLModelRepository
from dal.sql.forum.db_manager import get_db_session
from fastapi import HTTPException, status
from sqlmodel import SQLModel

class Controller:
    def __init__(self, Model: SQLModel):
        self.repository = SQLModelRepository(Model=Model)
    
    async def create(self, **new_data):
        try:
            async with get_db_session() as session:
                object = await self.repository.create(session=session, author_id=0, uid=0, **new_data)
                session.commit()
                session.refresh(object)
                
        except TypeError as e:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Item not found")
        
        return object.id or None
    
    async def read_by_id(self, id):
        try:
            async with get_db_session() as session:
                object = await self.repository.read(id==id, session=session)
        except TypeError as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Item not found")
        return object or None
    
    async def read_all(self):
        try:
            async with get_db_session() as session:
                objects = await self.repository.read(session=session)
        except TypeError as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Item not found")
        print(objects)
        return objects
    
    async def update(self, id, **new_data):
        async with get_db_session() as session:
            user = await self.repository.update(id=id, session=session, **new_data)
        return user or None
    
    async def delete(self, id):
        async with get_db_session() as session:
            user = await self.repository.delete(id=id, session=session)
        return user or None
    