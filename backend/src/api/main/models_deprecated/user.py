from typing import TYPE_CHECKING

from backend.src.dal.repositories.sqlmodel import UserRepository


class UserModel:
    def __init__(self):
        self.repository = UserRepository()

    async def create_user(self, **user_data):
        await self.repository.add(**user_data)

    async def get_user_by_id(self, user_id: int) -> dict:
        return (await self.repository.get(id=user_id))[0].to_dict()

    async def get_all_users(self) -> list[dict]:
        return list(map(lambda user: user.to_dict(), 
                        await self.repository.get())) 

    async def get_users_by_filter(self, **filter) -> list[dict]:
        return list(map(lambda user: user.to_dict(), 
                        await self.repository.get(**filter))) 

    async def update_user(self, user_id: int, **new_data):
        await self.repository.edit(user_id, **new_data)

    async def remove_user_by_id(self, user_id: int):
        await self.repository.remove(user_id)