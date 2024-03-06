ERROR_MESSAGE_USER_NOT_FOUND = 'User does not exist!'
ERROR_MESSAGE_WRONG_PASSWORD = 'Incorrect password!'
ERROR_MESSAGE_USER_ALREADY_EXISTS = 'User already exists!'
ERROR_MESSAGE_COMMENT_CONTENT_EMPTY = 'Comment empty!'
ERROR_MESSAGE_TOPIC_NAME_EMPTY = 'Topic name not defined!'
ERROR_MESSAGE_TOKEN_NOT_FOUND = 'Token not found in authorization header!'
ERROR_MESSAGE_INVALID_TOKEN = 'Token not found in authorization header!'
ERROR_MESSAGE_AUTHORIZATION_HEADER_NOT_FOUND = 'Authorization header not found!'
class UserNotFoundError(Exception):
    def __init__(self):
       self.message = ERROR_MESSAGE_USER_NOT_FOUND


class WrongPasswordError(Exception):
    def __init__(self):
       self.message = ERROR_MESSAGE_WRONG_PASSWORD


class UserAlreadyExistsError(Exception):
    def __init__(self):
       self.message = ERROR_MESSAGE_USER_ALREADY_EXISTS


class EmptyCommentContentError(Exception):
    def __init__(self):
       self.message = ERROR_MESSAGE_COMMENT_CONTENT_EMPTY


class EmptyTopicNameError(Exception):
    def __init__(self):
       self.message = ERROR_MESSAGE_TOPIC_NAME_EMPTY

class TokenNotFoundError(Exception):
    def __init__(self):
       self.message = ERROR_MESSAGE_TOKEN_NOT_FOUND

class InvalidTokenError(Exception):
    def __init__(self):
       self.message = ERROR_MESSAGE_INVALID_TOKEN

class AuthorizationHeaderNotFoundError(Exception):
    def __init__(self):
       self.message = ERROR_MESSAGE_AUTHORIZATION_HEADER_NOT_FOUND