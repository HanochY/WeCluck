from fastapi import APIRouter, Depends
from controllers.crud import Controller
from utils.exceptions import *
from entities.comment import CommentBase, CommentCreate, CommentRead, CommentUpdate
from dal.dbs.forum.models.comment import Comment
from typing_extensions import Annotated

router = APIRouter(prefix="/comment", tags=["comment"])

controller = Controller(Comment)

@router.post('/', status_code=201)
async def create_comment(comment: Annotated[CommentCreate, Depends]):
    response = await controller.create(comment)
    return response
        
@router.get('/', status_code=200, response_model=CommentBase)
async def read_comment(filter: Annotated[CommentRead, Depends]):
    response = await controller.read(filter)
    return response

@router.put('/', status_code=200)
async def update_comment(update: Annotated[CommentUpdate, Depends]):
    response = await controller.update(update)
    return response

@router.delete('/', status_code=204)
async def delete_comment(id: int):
    response = await controller.delete(id)
    return response