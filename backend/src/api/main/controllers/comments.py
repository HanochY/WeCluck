from controllers.crud import Controller
class CommentController(Controller):
    async def read(self, filter: int):
        with await get_db_session() as session:
            user = await self.repository.find(self.Model.id == filter['id'], session=session)[0]
        return user or None