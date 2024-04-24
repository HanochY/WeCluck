import os
import secrets

from pydantic_settings import BaseSettings

from config.environment import Environment


class AppConfig(BaseSettings):
    ip: str = "localhost"
    port: int = 5000
    environment: str = Environment.integration
    workers: int = os.cpu_count() * 2 + 1
    allowed_origins: list[str] = [
        f"http://{ip}",
        "http://localhost:5173",
    ]
    track_modifications: bool = False
    secret_key: str = secrets.token_urlsafe(32)