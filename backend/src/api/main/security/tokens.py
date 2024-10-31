from jwt import DecodeError, InvalidTokenError
from pydantic import BaseModel
from utils.jwts import encode_jwt, decode_jwt
from config.provider import ConfigProvider
from fastapi.security import OAuth2PasswordBearer

app_settings = ConfigProvider.forum_settings()
SECRET_KEY = app_settings.SECRET_KEY
ACCESS_TOKEN_EXPIRE_MINUTES = app_settings.ACCESS_TOKEN_EXPIRE_MINUTES
ALGORITHM = "HS256"
TOKEN_TYPE_BEARER = "bearer"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class FastAPIToken(BaseModel):
    token_value: str
    token_type: str
    def __init__(self, value):
        self.token_value = value

class FastAPIBearerToken(FastAPIToken):
    token_type: str = TOKEN_TYPE_BEARER
    
def encode_access_token(data: dict, expires_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    return(encode_jwt(data, expires_minutes, SECRET_KEY))


async def decode_access_token(token: str) -> str:
    data = decode_jwt(token, SECRET_KEY, ALGORITHM)
    uid: str = data.get("sub")
    if uid is None:
        raise DecodeError("UID is missing in token payload")
    return uid