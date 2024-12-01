from fastapi import APIRouter, Depends
from api.main.controllers.crud import Controller
from utils.exceptions import *
from dal.sql.forum.models.user import User, UserTable
from typing_extensions import Annotated


router = APIRouter(prefix="/user", tags=["user"])

controller = Controller(UserTable)

@router.post('/', status_code=201)
async def create_user(user: Annotated[User.Model.Create, Depends]):
    response = await controller.create(user)
    return response

@router.get('/all', status_code=200, response_model=User.Model.Public)
async def read_all_users():
    response = await controller.read()
    return response

@router.put('/', status_code=200)
async def update_user(update: Annotated[User.Model.Update, Depends]):
    response = await controller.update(update)
    return response

@router.delete('/', status_code=204)
async def delete_user(id: int):
    response = await controller.delete(id)
    return response