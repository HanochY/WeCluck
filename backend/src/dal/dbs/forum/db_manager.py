from sqlmodel import SQLModel, create_engine

from config.provider import ConfigProvider
from tables.comment import Comment
from tables.topic import Topic
from tables.user import User

forum_settings = ConfigProvider.forum_db_settings()

def init_forum_db():
    engine = create_engine(forum_settings.SQLITE_DATABASE_URI)
    SQLModel.metadata.create_all(engine)