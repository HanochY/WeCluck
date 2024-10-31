from functools import lru_cache

from config.app import ForumSettings, AppSettings
from config.db import ForumDBSettings, DBSettings
from config.metadata import Metadata


class ConfigProvider:
    @staticmethod
    @lru_cache(maxsize=1)
    def forum_settings() -> AppSettings:
        return ForumSettings()

    @staticmethod
    @lru_cache(maxsize=1)
    def forum_db_settings() -> DBSettings:
        return ForumDBSettings()

    @staticmethod
    @lru_cache(maxsize=1)
    def metadata() -> Metadata:
        return Metadata()