from fastapi import APIRouter, Depends
from api.main.controllers.crud import Controller
from utils.exceptions import *
from dal.sql.forum.models.comment import Comment, CommentTable
from typing_extensions import Annotated

router = APIRouter(prefix="/comment", tags=["comment"])

controller = Controller(CommentTable)

@router.post('/', status_code=201)
async def create_comment(comment: Annotated[Comment.Model.Create, Depends]):
    response = await controller.create(comment)
    return response
        
@router.get('/', status_code=200, response_model=list[Comment.Model.Public])
async def read_all_comments():
    response = await controller.read()
    return response

@router.put('/', status_code=200)
async def update_comment(update: Annotated[Comment.Model.Update, Depends]):
    response = await controller.update(update)
    return response

@router.delete('/', status_code=204)
async def delete_comment(id: int):
    response = await controller.delete(id)
    return response