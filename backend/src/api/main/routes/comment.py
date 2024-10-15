from fastapi import APIRouter, Depends
from controllers.comment import CommentController
from utils.exceptions import *
from entities.comment import CommentCreate, CommentRead, CommentUpdate
from typing_extensions import Annotated


router = APIRouter(prefix="/comments", tags=["comments"])

controller = CommentController()

@router.post('/')
async def post_comment(comment: CommentCreate):
    response, code = await controller.post_comment(current_user)
    return response, code
    
    
@router.get('/')
async def get_comment(comment: Annotated[CommentRead, Depends]):
    response, code = await controller.get_comments()
    return response, code