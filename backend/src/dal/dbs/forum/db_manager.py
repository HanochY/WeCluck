from sqlmodel import SQLModel, Session, create_engine

from config.provider import ConfigProvider
from tables.comment import Comment
from tables.topic import Topic
from tables.user import User

forum_db_settings = ConfigProvider.forum_db_settings()
engine = create_engine(forum_db_settings.SQLITE_DATABASE_URI)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_db_session():
    return Session(engine)