from typing import TYPE_CHECKING

from dal.sqlalchemy.repositories.comment import CommentRepository


class CommentModel:
    def __init__(self):
        self.repository = CommentRepository()
    
    async def create_comment(self, **comment_data):
        await self.repository.add(**comment_data)

    async def get_comment_by_id(self, comment_id: int) -> dict:
        return (await self.repository.get(id=comment_id))[0].to_dict()

    async def get_all_comments(self) -> list[dict]:
        return list(map(lambda comment: comment.to_dict(), 
                              await self.repository.get())) 

    async def get_comments_by_filter(self, **filter) -> list[dict]:
        return list(map(lambda comment: comment.to_dict(), 
                              await self.repository.get(**filter))) 

    async def update_comment(self, comment_id: int, **new_data):
        await self.repository.edit(comment_id, **new_data)

    async def remove_comment_by_id(self, comment_id: int):
        await self.repository.remove(comment_id)