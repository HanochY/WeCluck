import logging.config
import uvicorn
import logging
from config.provider import ConfigProvider
from utils.enums.environments import Environment

def run_server():
    main_settings = ConfigProvider.main_app_settings()
    logging_settings = ConfigProvider.logging_settings()
    logging.config.dictConfig(logging_settings.model_dump())
    uvicorn.run(
        "api.main.app:app",
        host=main_settings.ADDRESS,
        port=main_settings.PORT,
        reload=(main_settings.ENVIRONMENT == Environment.DEVELOPMENT),
        workers=main_settings.THREAD_COUNT,
        log_level = "DEBUG" if main_settings.DEBUG else "WARNING"
    )

if __name__ == "__main__":
    run_server()