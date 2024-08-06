from sqlmodel import SQLModel, create_engine

from config.provider import ConfigProvider
from dal.sqlalchemy.entities.comment import CommentEntity
from dal.sqlalchemy.entities.topic import TopicEntity
from dal.sqlalchemy.entities.user import UserEntity

forum_settings = ConfigProvider.forum_db_settings()

def init_forum_db():
    engine = create_engine(forum_settings.SQLITE_DATABASE_URI)
    SQLModel.metadata.create_all(engine)