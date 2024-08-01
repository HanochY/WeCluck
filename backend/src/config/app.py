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

    ADDRESS: str = "0.0.0.0"
    PORT: int = 5000
    TRACK_MODIFICATIONS: bool = False
    ALLOWED_ORIGINS: list[AnyUrl]
    ENVIRONMENT: Annotated[Environment, Field(validate_default=True)] = Environment.DEVELOPMENT
    WORKER_COUNT: int = os.cpu_count() * 2 + 1
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 604800 # 7 Days
    
    @field_validator('ENVIRONMENT')
    @classmethod
    def must_be_environment(cls, v: Environment | str) -> Environment:
        if isinstance(v, Environment):
            return v
        elif isinstance(v, str):
            return Environment(v.upper())