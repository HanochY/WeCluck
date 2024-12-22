from collections.abc import Sequence
from uuid import UUID
from utils.exceptions import *
from dal.sql.repository import SQLModelRepository
from dal.sql.forum.db_manager import get_db_session
from fastapi import HTTPException, status
from api.main.controllers._crud import Controller
from dal.schema.resources.user import UserPublic, UserFullInput, UserPartialInput
from dal.sql.forum.resources.user import DBUser

class UserController(Controller[DBUser, UserFullInput, UserPartialInput, UserPublic]):
    db_model = type[DBUser]
    
    def __init__(self) -> None:
        self.repository = SQLModelRepository(Model=self.db_model)
    
    async def create(self, data: UserFullInput) -> UUID | None:
        try:
            async for session in get_db_session():
                object: DBUser = await self.repository.create(session=session, author_id=0, **data)
                await session.commit()
                await session.refresh(object)
                
        except TypeError as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Unprocessable entity!")
        
        if object: return object.id 
        else: return None
    
    async def read_by_id(self, id: UUID) -> UserPublic | None:
        async for session in get_db_session():
            results: Sequence[DBUser] | None = await self.repository.read(filter=id==id, session=session)  
        if results: return UserPublic(results[0])
        else: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    
    async def read_all(self) -> list[UserPublic] | None:
        async for session in get_db_session():
            results: Sequence[DBUser] | None = await self.repository.read(session=session)
        if results: return [UserPublic(object) for object in results]
        else: raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    
    async def update(self, id: UUID, new_data: UserPartialInput) -> None:
        try:
            async for session in get_db_session():
                await self.repository.update(id=id, session=session, **new_data)
            return None
        except TypeError:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Unprocessable entity!")
    
    async def delete(self, id: UUID) -> None:
        async for session in get_db_session():
            await self.repository.delete(id=id, session=session)
        return None
    
    async def undelete(self, id: UUID) -> None:
        async for session in get_db_session():
            await self.repository.undelete(id=id, session=session)
        return None
    
    async def hard_delete(self, id: UUID) -> None:
        async for session in get_db_session():
            await self.repository.hard_delete(id=id, session=session)
        return None
    
    