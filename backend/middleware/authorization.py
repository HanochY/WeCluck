from functools import wraps
import jwt
from utils.exceptions import *
from flask import request
from flask import current_app
from models.user import *


def read_token(request):
    if "Authorization" in request.headers:
        token = request.headers["Authorization"].split(" ")[1]
        if token:
            return token
        else:
            raise TokenNotFoundError
    else:
        raise AuthorizationHeaderNotFoundError

def get_user_from_token(token):
    token_data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
    user = get_user_by_id(token_data["user_id"])
    if user:
        return user
    else:
        raise InvalidTokenError

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            token = read_token(request) # Bearer <token> -> <token>
        except (TokenNotFoundError, AuthorizationHeaderNotFoundError) as error:
            return {
                "message": "Authentication failed!",
                "data": None,
                "error": str(error)
            }, 401
        try:
            current_user = get_user_from_token(token)
        except InvalidTokenError as error:
            return {
                "message": "Authentication failed!",
                "data": None,
                "error": str(error)
            }, 401

        return f(current_user, *args, **kwargs)

    return decorated