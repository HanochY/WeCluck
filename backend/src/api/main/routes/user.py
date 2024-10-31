from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from api.main.controllers.crud import Controller
from utils.exceptions import *
from entities.user import UserPublic, UserCreate, UserUpdate
from dal.models.user import User
from dal.models.filters.user import UserFilter
from typing_extensions import Annotated

router = APIRouter(prefix="/user", tags=["user"])

controller = Controller(User)

@router.post('/', status_code=201)
async def create_user(user: Annotated[UserCreate, Depends]):
    response = await controller.create(user)
    return response
        
@router.get('/', status_code=200, response_model=UserPublic)
async def read_user_public(filter: Annotated[UserFilter, FilterDepends]):
    response = await controller.read(filter)
    return response

@router.put('/', status_code=200)
async def update_user(update: Annotated[UserUpdate, Depends]):
    response = await controller.update(update)
    return response

@router.delete('/', status_code=204)
async def delete_user(id: int):
    response = await controller.delete(id)
    return response