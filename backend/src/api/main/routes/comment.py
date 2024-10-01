from fastapi import APIRouter, Depends
from controllers.comment import CommentController
from utils.exceptions import *
from middleware.authorization import token_required

router = APIRouter(prefix="/comments", tags=["comments"])

controller = CommentController()

@router.post('/')
@token_required
async def post_comment(current_user):
    response, code = await controller.post_comment(current_user)
    return response, code
    
    
@router.get('/')
@token_required
async def post_comment():
    response, code = await controller.get_comments()
    return response, code