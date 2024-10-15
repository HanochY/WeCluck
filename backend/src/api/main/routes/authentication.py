from fastapi import APIRouter, Depends

import controllers.authentication as controller
from src.api.main.security.tokens import FastAPIBearerToken
from src.dal.dbs.forum.db_manager import get_db_session

router = APIRouter(prefix="/token", tags=["token"])


@router.post("/")
async def login_token(token: FastAPIBearerToken = Depends(controller.login_for_access_token)):
    return token