from collections.abc import Sequence
from uuid import UUID
from backend.src.dal.sql.forum.tables._common import SQLModelCommon
from utils.exceptions import *
from dal.sql.repository import SQLModelRepository
from dal.sql.forum.db_manager import get_db_session
from fastapi import HTTPException, status
from api.main.controllers._crud import Controller
from dal.sql.forum.tables.user import UserModels, User

class UserController(Controller[User, UserModels.Create, UserModels.Update, UserModels.Public]):
    db_model = type[User]
    
    def __init__(self) -> None:
        self.repository = SQLModelRepository(Model=self.db_model)
    
    async def create(self, data: UserModels.Create) -> UUID | None:
        try:
            async for session in get_db_session():
                object: User = await self.repository.create(session=session, author_id=0, **data)
                await session.commit()
                await session.refresh(object)
                
        except TypeError as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Unprocessable entity!")
        
        if object: return object.id 
        else: return None
    
    async def read_by_id(self, id: UUID) -> UserModels.Public | None:
        try:
            async for session in get_db_session():
                results: Sequence[SQLModelCommon] | None = await self.repository.read(filter=id==id, session=session)
        except TypeError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        if results: return UserModels.Public(results[0])
        else: return None
    
    async def read_all(self) -> list[UserModels.Public] | None:
        try:
            async for session in get_db_session():
                results: Sequence[User] | None = await self.repository.read(session=session)
        except TypeError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        if results: return [UserModels.Public(object) for object in results]
        else: return None
    
    async def update(self, id: UUID, new_data: UserModels.Update) -> None:
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
    
    