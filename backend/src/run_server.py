import uvicorn

from src.config.provider import ConfigProvider
from src.utils.enums import Environment

def run_server():
    forum_settings = ConfigProvider.forum_settings()
    uvicorn.run(
        "api.app:app",
        host=forum_settings.DOMAIN,
        port=forum_settings.PORT,
        reload=(forum_settings.ENVIRONMENT == Environment.DEVELOPMENT),
        workers=forum_settings.THREAD_COUNT if not dev_environment else None
    )


if __name__ == "__main__":
    run_server()