from fastapi import APIRouter, Depends
from controllers.user import UserController
from utils.exceptions import *

router = APIRouter(prefix="/topics", tags=["topics"])

controller = UserController()

@router.post('/')
async def users():
    response, code = await controller.register()
    return response, code 
