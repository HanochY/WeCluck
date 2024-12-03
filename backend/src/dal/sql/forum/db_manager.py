from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession 
from sqlalchemy.orm import sessionmaker
from config.provider import ConfigProvider
from contextlib import asynccontextmanager
from dal.sql.forum.tables.comment import Comment
from dal.sql.forum.tables.topic import Topic
from dal.sql.forum.tables.user import User

forum_db_settings = ConfigProvider.forum_db_settings()
DATABASE_URL = forum_db_settings.SQLITE_DATABASE_URI.replace("sqlite://", "sqlite+aiosqlite://")
engine = create_async_engine(DATABASE_URL)

AsyncSessionLocal = sessionmaker(bind=engine, 
                                 class_=AsyncSession,
                                 expire_on_commit=False)
@asynccontextmanager
async def get_db_session():
    async with AsyncSessionLocal() as session: 
        yield session

def create_db():
    SQLModel.metadata.create_all(engine)