from sqlmodel import SQLModel, Session, create_engine

from config.provider import ConfigProvider
from models.comment import Comment
from models.topic import Topic
from models.user import User

forum_db_settings = ConfigProvider.forum_db_settings()
engine = create_engine(forum_db_settings.SQLITE_DATABASE_URI)

async def get_db_session():
    return Session(engine)

def create_db():
    SQLModel.metadata.create_all(engine)