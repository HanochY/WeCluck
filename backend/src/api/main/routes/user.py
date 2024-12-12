from fastapi import APIRouter, Depends
from api.main.controllers.crud import Controller
from utils.exceptions import *
from dal.sql.forum.tables.user import UserModels, User
from typing_extensions import Annotated
from uuid import UUID

router = APIRouter(prefix="/user", tags=["user"])

controller = Controller(User)

@router.post('/', status_code=201)
async def create_user(user: Annotated[UserModels.Create, Depends]):
    response = await controller.create(**dict(user))
    return response

@router.get('/all', status_code=200, response_model=UserModels.Public)
async def read_all_users():
    response = await controller.read_all()
    return response

@router.put('/', status_code=200)
async def update_user(update: Annotated[UserModels.Update, Depends]):
    response = await controller.update(**dict(update))
    return response

@router.delete('/', status_code=204)
async def delete_user(id: UUID):
    response = await controller.delete(id)
    return response