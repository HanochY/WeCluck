from pydantic_settings import BaseSettings

from utils.enums.db_vendors import DBVendor
from utils.enums.environments import Environment
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    
    SERVER: str = "localhost"
    PORT: int | None
    USER: str | None
    PASSWORD: str | None
    NAME: str

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

class ForumDBSettings(DBSettings):
    model_config = SettingsConfigDict(env_file='.env',
                                      env_prefix='FORUM_DB_',
                                      env_ignore_empty=True,
                                      extra="ignore")
    NAME: r"development-forum.sqlite3"