
from config.provider import ConfigProvider
from dal.sql.forum.tables._common import SQLModelCommon
from dal.sql.forum.tables.comment import Comment
from dal.sql.forum.tables.topic import Topic
from dal.sql.forum.tables.user import User

import contextlib
from typing import Any, AsyncIterator
#from _collections_abc import AsyncIterator
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

forum_db_settings = ConfigProvider.forum_db_settings(production=False)
DATABASE_URL = forum_db_settings.URI.replace("sqlite://", "sqlite+aiosqlite://")

class DatabaseSessionManager:
    def __init__(self, host: str, engine_kwargs: dict[str, Any] = {}):
        self._engine = create_async_engine(host, **engine_kwargs)
        self._sessionmaker = async_sessionmaker(autocommit=False, bind=self._engine)

    async def close(self):
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")
        await self._engine.dispose()

        self._engine = None
        self._sessionmaker = None

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")

        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._sessionmaker is None:
            raise Exception("DatabaseSessionManager is not initialized")

        session = self._sessionmaker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
            
    async def init_db(self):
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")
        async with self._engine.begin() as conn: 
            await conn.run_sync(SQLModelCommon.metadata.create_all)


session_manager = DatabaseSessionManager(DATABASE_URL)


async def get_db_session():
    async with session_manager.session() as session:
        yield session