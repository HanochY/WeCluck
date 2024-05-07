from pydantic.dataclasses import dataclass

from config.app import APP_CONFIGS, AppConfig
from config.db import DB_CONFIGS, DBConfig
from config.metadata import Metadata


@dataclass
class ConfigManager:
    app: AppConfig
    
    db: DBConfig
    
    metadata: Metadata

app_config = APP_CONFIGS[AppConfig().environment]
db_config = DB_CONFIGS[AppConfig().environment]
config = ConfigManager(app = app_config,
                       db = db_config,
                       metadata = Metadata())