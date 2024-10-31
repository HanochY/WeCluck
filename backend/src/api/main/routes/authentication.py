from fastapi import APIRouter, Depends

from api.main.controllers.authentication import AuthenticationController
from api.main.security.tokens import FastAPIBearerToken


router = APIRouter(prefix="/token", tags=["token"])
controller = AuthenticationController()

@router.post("/")
async def login_token(token: FastAPIBearerToken = 
                      Depends(controller.login_for_access_token)) -> FastAPIBearerToken:
    return token