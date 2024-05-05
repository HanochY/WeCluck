import os
import secrets

from pydantic_settings import BaseSettings

from utils.enums.environments import Environment


class AppConfig(BaseSettings):
    host: str = "localhost"
    port: int = 5000
    environment: str = Environment.integration
    track_modifications: str = True
    workers: int = os.cpu_count() * 2 + 1
    threaded: bool = False
    allowed_origins: list[str] = [
        f"http://{host}",
        "http://localhost:5173",
    ]
    secret_key: str = secrets.token_urlsafe(32)