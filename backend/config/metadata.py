from pydantic_settings import BaseSettings


class Metadata(BaseSettings):
    NAME: str = "WeCluck"
    DESCRIPTION: str = "Chicken-based per-topic forum."
    AUTHOR: str = "Hanoch Y"
    VERSION: str = "1.0.0"