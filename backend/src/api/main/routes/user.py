from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from api.main.controllers.crud import Controller
from utils.exceptions import *
from dal._schema.entities.user import User
from typing_extensions import Annotated
from typing import Type

UserCreate = Type(User.create)
UserUpdate = NewType("UserCreate", User.update)


router = APIRouter(prefix="/user", tags=["user"])

controller = Controller()

@router.post('/', status_code=201)
async def create_user(user: Annotated[UserCreate, Depends]):
    response = await controller.create(user)
    return response

@router.put('/', status_code=200)
async def update_user(update: Annotated[UserUpdate, Depends]):
    response = await controller.update(update)
    return response

@router.delete('/', status_code=204)
async def delete_user(id: int):
    response = await controller.delete(id)
    return response