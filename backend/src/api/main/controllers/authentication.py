from datetime import timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from utils.passwords import verify_password
from api.main.security.tokens import (
    FastAPIBearerToken,
    encode_access_token,
    decode_access_token,
    oauth2_scheme,
)
from dal.sql.forum.tables.user import UserModels
from dal.sql.forum.tables.user import User
from dal.sql.repository import SQLModelRepository, Session
from dal.sql.forum.db_manager import get_db_session
from config.provider import ConfigProvider
from uuid import UUID

app_settings = ConfigProvider.main_app_settings()

class AuthenticationController:
    
    repository = SQLModelRepository(Model=User)
    
    async def get_user(self, uid: UUID, session: Session) -> UserModels.Public:
        user = await self.repository.find(User.id == uid, session=session)[0]
        return user or None

    async def find_user_by_username(self, username: str, session: Session) -> UserModels.Public:
        user = await self.repository.find(User.name == username, session=session)[0]
        return user or None

    async def get_current_user(self, token: str = Depends(oauth2_scheme)) -> UserModels.Public:
        decoded_token_uid = await decode_access_token(token)
        with await get_db_session() as session:
            user = await self.get_user(User.id == decoded_token_uid, session)
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Authentication failed invalid credentials")
        return user

    async def authenticate_for_access_token(self, form_data: OAuth2PasswordRequestForm = Depends()):
        with await get_db_session() as session:
            user = await self.find_user_by_username(form_data.username, session)
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
        