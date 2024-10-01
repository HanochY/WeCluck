from datetime import datetime, timedelta, timezone

import jwt
from jwt import InvalidTokenError

    
def encode_jwt(data: dict, expires_minutes: int, secret_key: str, algorithm: str) -> str:
    plaintext = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    plaintext.update({"exp": expire})
    token = jwt.encode(plaintext, secret_key, algorithm=algorithm)
    return token


async def decode_jwt(token: str, secret_key: str, algorithm: str) -> str:
    try:
        data = jwt.decode(token, secret_key, algorithms=[algorithm])
    except InvalidTokenError:
        raise InvalidTokenError("Invalid token")
    return data