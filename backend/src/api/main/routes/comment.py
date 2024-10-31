from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from api.main.controllers.crud import Controller
from utils.exceptions import *
from entities.comment import CommentBase, CommentCreate, CommentUpdate
from dal.models.comment import Comment
from dal.models.filters.comment import CommentFilter
from typing_extensions import Annotated

router = APIRouter(prefix="/comment", tags=["comment"])

controller = Controller(Comment)

@router.post('/', status_code=201)
async def create_comment(comment: Annotated[CommentCreate, Depends]):
    response = await controller.create(comment)
    return response
        
@router.get('/', status_code=200, response_model=CommentBase)
async def read_comment(filter: Annotated[CommentFilter, FilterDepends]):
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