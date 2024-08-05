import os
import secrets
from typing import Annotated

from pydantic import AnyUrl, field_validator, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from utils.enums.environments import Environment

class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env',
                                      env_prefix='BACKEND_',
                                      env_ignore_empty=True,
                                      extra="ignore")

    ENVIRONMENT: Annotated[Environment, Field(validate_default=True)] = Environment.DEVELOPMENT
    ADDRESS: str
    PORT: int
    TRACK_MODIFICATIONS: bool
    DEBUG: bool
    ALLOWED_ORIGINS: list[AnyUrl]
    THREAD_COUNT: int
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_SECONDS: int
    if ENVIRONMENT == Environment.DEVELOPMENT:
        ADDRESS = "localhost"
        PORT = 5000
        TRACK_MODIFICATIONS = True
        DEBUG = True
        ALLOWED_ORIGINS = ["http://localhost", "http://localhost:5173", "https://localhost", "https://localhost:5173"]
        THREAD_COUNT = 1
        SECRET_KEY = secrets.token_urlsafe(32)
        ACCESS_TOKEN_EXPIRE_SECONDS = 604800 # 7 Days
    elif ENVIRONMENT == Environment.PRODUCTION:
        ADDRESS = "0.0.0.0"
        PORT = 443
        TRACK_MODIFICATIONS = False
        DEBUG = False
        THREAD_COUNT = os.cpu_count() * 2 + 1
        SECRET_KEY = secrets.token_urlsafe(32)
        ACCESS_TOKEN_EXPIRE_SECONDS = 604800 # 7 Days
    
    @field_validator('ENVIRONMENT')
    @classmethod
    def must_be_environment(cls, v: Environment | str) -> Environment:
        if isinstance(v, Environment):
            return v
        elif isinstance(v, str):
            return Environment(v.upper())