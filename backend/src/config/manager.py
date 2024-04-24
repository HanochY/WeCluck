from pydantic.dataclasses import dataclass

from config.app import AppConfig
from config.db import DB_CONFIGS, DBConfig
from config.metadata import Metadata


@dataclass
class ConfigManager:
    app: AppConfig
    
    db: DBConfig
    
    metadata: Metadata


db_config = DB_CONFIGS[AppConfig().environment]
config = ConfigManager(app = AppConfig(),
                       db = db_config,
                       metadata = Metadata())