import os
import secrets
import json
from typing import Annotated

from pydantic import AnyUrl, field_validator, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from utils.enums.environments import Environment

class AppSettings(BaseSettings):
    ENVIRONMENT: Annotated[Environment, Field(validate_default=True)] = Environment.DEVELOPMENT
    ADDRESS: str
    PORT: int
    TRACK_MODIFICATIONS: bool
    DEBUG: bool
    ALLOWED_ORIGINS: list[AnyUrl]
    THREAD_COUNT: int
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ACCESS_TOKEN_ALGORITHM: str
    if ENVIRONMENT == Environment.DEVELOPMENT:
        ADDRESS = "localhost"
        TRACK_MODIFICATIONS = True
        DEBUG = True
        ALLOWED_ORIGINS = ["http://localhost", "http://localhost:5173", "https://localhost", "https://localhost:5173"]
        THREAD_COUNT = 1
        SECRET_KEY = secrets.token_urlsafe(32)
        ACCESS_TOKEN_EXPIRE_MINUTES = 7200 # 5 Days
        ACCESS_TOKEN_ALGORITHM = "HS256"
    elif ENVIRONMENT == Environment.PRODUCTION:
        ADDRESS = "0.0.0.0"
        TRACK_MODIFICATIONS = False
        DEBUG = False
        THREAD_COUNT = os.cpu_count() * 2 + 1
        SECRET_KEY = secrets.token_urlsafe(32)
        ACCESS_TOKEN_EXPIRE_MINUTES = 30
        ACCESS_TOKEN_ALGORITHM = "HS256"
    
    @field_validator('ENVIRONMENT', mode="before")
    @classmethod
    def str_to_environment(cls, v: str) -> Environment:
        return Environment(v.upper())
    
    @field_validator('ALLOWED_ORIGINS', mode="before")
    @classmethod
    def str_to_url_list(cls, v: str | list[AnyUrl]) -> list[AnyUrl]:
        if isinstance(v, str):
            return json.loads(v)
        else:
            return v
    
    @field_validator('ALLOWED_ORIGINS', mode="after")
    @classmethod
    def strip_urls(cls, v: list[AnyUrl]) -> list[AnyUrl]:
        return [AnyUrl(str(i).strip("/")) for i in v]
        
            

class ForumSettings(AppSettings):
    model_config = SettingsConfigDict(env_file='.env',
                                      env_prefix='FORUM_BACKEND_',
                                      env_ignore_empty=True,
                                      extra="ignore")
    PORT: int = 5000