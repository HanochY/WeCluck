from fastapi import APIRouter, Depends

import controllers.authentication as controller
from src.api.main.security.tokens import FastAPIBearerToken


router = APIRouter(prefix="/token", tags=["token"])


@router.post("/")
async def login_token(token: FastAPIBearerToken = 
                      Depends(controller.login_for_access_token)) -> FastAPIBearerToken:
    return token