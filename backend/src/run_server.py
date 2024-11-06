import uvicorn

from config.provider import ConfigProvider
from utils.enums.environments import Environment

def run_server():
    forum_settings = ConfigProvider.forum_settings()
    uvicorn.run(
        "api.main.app:app",
        host=forum_settings.ADDRESS,
        port=forum_settings.PORT,
        reload=(forum_settings.ENVIRONMENT == Environment.DEVELOPMENT),
        workers=forum_settings.THREAD_COUNT
    )


if __name__ == "__main__":
    from entities.join import join
    from entities.comment import CommentRead
    from entities.topic import TopicRead
    print(join(CommentRead, TopicRead, 'topic_id').model_fields)
    #run_server()