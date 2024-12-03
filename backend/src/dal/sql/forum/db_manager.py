from sqlmodel import SQLModel, Session, create_engine

from config.provider import ConfigProvider
from dal.sql.forum.tables.comment import Comment
from dal.sql.forum.tables.topic import Topic
from dal.sql.forum.tables.user import User

forum_db_settings = ConfigProvider.forum_db_settings()
engine = create_engine(forum_db_settings.SQLITE_DATABASE_URI)

async def get_db_session():
    return Session(engine)

def create_db():
    SQLModel.metadata.create_all(engine)