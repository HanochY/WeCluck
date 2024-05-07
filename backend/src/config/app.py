import secrets

from pydantic_settings import BaseSettings

from utils.enums.environments import Environment


class AppConfig(BaseSettings):
    host: str
    port: int
    environment: str
    track_modifications: bool
    debug: bool
    threaded: bool
    allowed_origins: list[str]
    secret_key: str

class IntegrationAppConfig(AppConfig):
    host: str = "localhost"
    port: int = 5000
    environment: str = Environment.integration
    track_modifications: bool = True
    debug: bool = True
    threaded: bool = False
    allowed_origins: list[str] = [
        f"http://{host}",
        "http://localhost:5173",
    ]
    secret_key: str = secrets.token_urlsafe(32)

class ProductionAppConfig(AppConfig):
    pass

APP_CONFIGS = {
    Environment.integration: IntegrationAppConfig(),
    Environment.production: ProductionAppConfig()
}