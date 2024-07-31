import secrets

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import HttpUrl, AnyUrl, field_validator

from utils.enums.environments import Environment


class AppConfig(BaseSettings):
    url: HttpUrl
    environment: str
    track_modifications: bool
    debug: bool
    threaded: bool
    allowed_origins: list[AnyUrl]
    secret_key: str
    
    @field_validator("environment")
    @classmethod
    def parse_environment(cls, environment) -> str:
        match type(environment).__name__:
            case str.__name__:
                return Environment(environment.lower())
            case Environment.__name__:
                return environment
            case _:
                raise ValueError(environment)
'''
class IntegrationAppConfig = AppConfig(
    url = "http://localhost:5000"
    environment = Environment.integration
    track_modifications = True
    debug = True
    threaded = False
    allowed_origins = [
        "http://localhost",
        "http://localhost:5173",
    ]
    secret_key = secrets.token_urlsafe(32)

class ProductionAppConfig(AppConfig):
    url = "http://localhost:5000"
    environment: str = Environment.production
    track_modifications: bool = True
    debug: bool = True
    threaded: bool = False
    allowed_origins: list[str] = [
        "http://localhost",
        "http://localhost:5173",
    ]
    secret_key: str = secrets.token_urlsafe(32)

APP_CONFIGS = {
    Environment.integration: IntegrationAppConfig(),
    Environment.production: ProductionAppConfig()
}
'''
