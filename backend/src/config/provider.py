from functools import lru_cache

from config.app import AppSettings
from config.db import DBSettings
from config.metadata import Metadata


class ConfigProvider:
    @staticmethod
    @lru_cache(maxsize=1)
    def app_settings() -> AppSettings:
        return AppSettings()

    @staticmethod
    @lru_cache(maxsize=1)
    def db_settings() -> DBSettings:
        return DBSettings()

    @staticmethod
    @lru_cache(maxsize=1)
    def metadata() -> Metadata:
        return Metadata()