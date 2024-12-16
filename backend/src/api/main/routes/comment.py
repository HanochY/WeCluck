from fastapi import APIRouter, Depends
from backend.src.api.main.controllers.comment import CommentController
from backend.src.dal._schema.resources.comment import Public
from utils.exceptions import *
from dal.sql.forum.tables.comment import CommentModels, Comment
from typing_extensions import Annotated
from uuid import UUID

router = APIRouter(prefix="/comment", tags=["comment"])

controller = CommentController()

@router.post('/', status_code=201)
async def create_comment(comment: Annotated[CommentModels.Create, Depends]) -> UUID | None:
    response: UUID | None = await controller.create(data=comment)
    return response
        
@router.get('/all', status_code=200, response_model=list[CommentModels.Public])
async def read_all_comments() -> list[CommentModels.Public] | None:
    response: list[CommentModels.Public] | None = await controller.read_all()
    return response

@router.put('/', status_code=200)
async def update_comment(id: UUID, comment_update: Annotated[CommentModels.Update, Depends]) -> None:
    await controller.update(id=id, new_data=comment_update)

@router.delete('/', status_code=204)
async def delete_comment(id: UUID) -> None:
    await controller.delete(id=id)
