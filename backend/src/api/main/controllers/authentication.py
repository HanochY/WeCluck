from datetime import timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.utils.passwords import verify_password
from src.api.main.security.tokens import (
    FastAPIBearerToken,
    encode_access_token,
    decode_access_token,
    oauth2_scheme,
)
from src.entities.user import UserRead
from src.dal.repositories.sqlmodel import SQLModelRepository, Session
from src.dal.dbs.forum.db_manager import get_db_session
from dal.dbs.forum.models.user import User
from config.provider import ConfigProvider

app_settings = ConfigProvider.forum_settings()
user_repository = SQLModelRepository(Model=User)

async def get_user(uid: int, session: Session) -> User:
    user = await user_repository.find(User.id == uid, session=session)[0]
    return user or None

async def find_user_by_username(username: str, session: Session) -> User:
    user = await user_repository.find(User.name == username, session=session)[0]
    return user or None

async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserRead:
    decoded_token_uid = await decode_access_token(token)
    with await get_db_session() as session:
        user = await get_user(User.id == decoded_token_uid, session)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Authentication failed invalid credentials")
    return user

async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> FastAPIBearerToken:
    with await get_db_session() as session:
        user = await find_user_by_username(form_data.username, session)
    if user:
        correct_password_hash = user.password
        if verify_password(form_data.password, correct_password_hash):
            token = encode_access_token(
                data={"sub": user.id}, 
                expires_delta=timedelta(
                    minutes=app_settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            )
            return FastAPIBearerToken(token)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
    