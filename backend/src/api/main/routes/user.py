from fastapi import APIRouter, Depends, Security
from backend.src.api.main.controllers.user import UserController
from api.main.controllers.authentication import AuthenticationController
from backend.src.dal._schema.resources.user import Public
from utils.exceptions import *
from dal.sql.forum.tables.user import UserModels, User
from typing_extensions import Annotated
from uuid import UUID

router = APIRouter(prefix="/user", tags=["user"])

controller = UserController()
auth_controller = AuthenticationController() # to be moved

@router.post('/', status_code=201)
async def create_user(user: Annotated[UserModels.Create, Depends]) -> UUID | None:
    response = await controller.create(data=user)
    return response

@router.get('/me', status_code=200, response_model=UserModels.Public)
async def read_current_user(current_user: Annotated[UserModels.Public,
                                                    Security(auth_controller.get_current_user, 
                                                    scopes=["self"])]) -> UserModels.Public:
    return current_user

@router.get('/all', status_code=200, response_model=UserModels.Public)
async def read_all_users() -> list[UserModels.Public] | None:
    response: list[UserModels.Public] | None = await controller.read_all()
    return response

@router.put('/', status_code=200)
async def update_user(id: UUID, user_update: Annotated[UserModels.Update, Depends]) -> None:
    await controller.update(id=id, new_data=user_update)
 

@router.delete('/', status_code=204)
async def delete_user(id: UUID) -> None:
    await controller.delete(id=id)
