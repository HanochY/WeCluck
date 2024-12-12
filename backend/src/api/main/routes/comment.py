from fastapi import APIRouter, Depends
from api.main.controllers.crud import Controller
from utils.exceptions import *
from dal.sql.forum.tables.comment import CommentModels, Comment
from typing_extensions import Annotated
from uuid import UUID

router = APIRouter(prefix="/comment", tags=["comment"])

controller = Controller(Comment)

@router.post('/', status_code=201)
async def create_comment(comment: Annotated[CommentModels.Create, Depends]):
    response = await controller.create(**dict(comment))
    return response
        
@router.get('/all', status_code=200, response_model=list[CommentModels.Public])
async def read_all_comments():
    response = await controller.read_all()
    return response

@router.put('/', status_code=200)
async def update_comment(update: Annotated[CommentModels.Update, Depends]):
    response = await controller.update(**dict(update))
    return response

@router.delete('/', status_code=204)
async def delete_comment(id: UUID):
    response = await controller.delete(id)
    return response