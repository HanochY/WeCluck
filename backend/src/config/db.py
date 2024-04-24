from pydantic_settings import BaseSettings
from enum import auto
from strenum import StrEnum

from config.environment import Environment

class DBVendor(StrEnum):
    sqlite: str = auto()

class DBConfig(BaseSettings):
    vendor: str
    host: str
    port: str
    name: str
    username: str
    password: str
    


class IntegrationDBConfig(DBConfig):
    vendor: str = DBVendor.sqlite
    host: str = ""
    port: str = ""
    name: str = "integration-KoolKluckerDB.sqlite3"
    username: str = ""
    password: str = ""

class ProductionDBConfig(DBConfig):
    vendor: str = DBVendor.sqlite
    host: str = ""
    port: str = ""
    name: str = "production-KoolKluckerDB.sqlite3"
    username: str = ""
    password: str = ""

DB_CONFIGS = {
    Environment.integration: IntegrationDBConfig(),
    Environment.production: ProductionDBConfig()
}
