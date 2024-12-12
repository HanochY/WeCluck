from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession 
from sqlalchemy.orm import sessionmaker
from config.provider import ConfigProvider
from contextlib import asynccontextmanager
from dal.sql.forum.tables._common import SQLModelCommon
from dal.sql.forum.tables.comment import Comment
from dal.sql.forum.tables.topic import Topic
from dal.sql.forum.tables.user import User

forum_db_settings = ConfigProvider.forum_db_settings(production=False)
DATABASE_URL = forum_db_settings.URI.replace("sqlite://", "sqlite+aiosqlite://")

engine = create_async_engine(DATABASE_URL)

AsyncSessionLocal = sessionmaker(bind=engine, 
                                 class_=AsyncSession,
                                 expire_on_commit=False)
@asynccontextmanager
async def get_db_session():
    async with AsyncSessionLocal() as session: 
        yield session

async def init_db(): 
    async with engine.begin() as conn: 
        await conn.run_sync(SQLModelCommon.metadata.create_all)