from fastapi import APIRouter, Depends
from controllers.user import UserController
from utils.exceptions import *
from entities.user import UserCreate, UserRead, UserUpdate
from typing_extensions import Annotated

router = APIRouter(prefix="/user", tags=["topics"])

controller = UserController()

@router.post('/')
async def post_user(user: UserCreate):
    response, code = await controller.post_user()
    return response, code
    
    
@router.get('/')
async def get_user(user: Annotated[UserRead, Depends]):
    response, code = await controller.get_users()
    return response, code