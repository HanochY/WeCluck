from pydantic.dataclasses import dataclass

from config.app import APP_CONFIGS, AppConfig
from config.db import DB_CONFIGS, DBConfig
from config.metadata import Metadata
from utils.enums.environments import Environment

@dataclass
class ConfigManager:
    app: AppConfig
    
    db: DBConfig
    
    metadata: Metadata

environment = Environment.integration
app_config = APP_CONFIGS[environment]
db_config = DB_CONFIGS[environment]
config = ConfigManager(app = app_config,
                       db = db_config,
                       metadata = Metadata())