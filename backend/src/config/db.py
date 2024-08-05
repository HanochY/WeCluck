from pydantic_settings import BaseSettings

from utils.enums.db_vendors import DBVendor
from utils.enums.environments import Environment
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env',
                                      env_prefix='DB_',
                                      env_ignore_empty=True,
                                      extra="ignore")
    SERVER: str = "localhost"
    PORT: int | None = None
    USER: str | None = None
    PASSWORD: str | None = None
    NAME: str = "integration-KoolKluckerDB2.sqlite3"

    @computed_field
    @property
    def MONGO_DATABASE_URI(self) -> str:
        uri = f"mongodb://{self.USER}:{self.PASSWORD}@{self.SERVER}:{self.PORT}/{self.NAME}"
        return uri
    
    @computed_field
    @property
    def SQLITE_DATABASE_URI(self) -> str:
        uri = f"sqlite:///{self.NAME}"
        return uri