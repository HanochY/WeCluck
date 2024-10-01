from fastapi import APIRouter, Depends

import controllers.authentication as controller


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token/")
async def login_token(token = Depends(controller.login_for_access_token)):
    return token