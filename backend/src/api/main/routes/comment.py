from fastapi import APIRouter, Depends
from api.main.controllers.comment import CommentController
from utils.exceptions import *
from dal.schema.resources.comment import CommentPublic, CommentFullInput, CommentPartialInput
from typing_extensions import Annotated
from uuid import UUID

router = APIRouter(prefix="/comment", tags=["comment"])

controller = CommentController()

@router.post('/', status_code=201)
async def create_comment(comment: Annotated[CommentFullInput, Depends]) -> UUID | None:
    response: UUID | None = await controller.create(data=comment)
    return response
        
@router.get('/all', status_code=200, response_model=list[CommentPublic])
async def read_all_comments() -> list[CommentPublic] | None:
    response: list[CommentPublic] | None = await controller.read_all()
    return response

@router.get('/{id}', status_code=200, response_model=CommentPublic)
async def read_comment_by_id() -> list[CommentPublic] | None:
    try:
        response: CommentPublic | None = await controller.read_by_id()
        return response
    except Exception as e:
        print(e)
        
@router.patch('/{id}', status_code=200)
async def update_comment(id: UUID, comment_update: Annotated[CommentPartialInput, Depends]) -> None:
    await controller.update(id=id, new_data=comment_update)
    return None

@router.delete('/{id}', status_code=204)
async def delete_comment(id: UUID) -> None:
    await controller.delete(id=id)
    return None
