from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from .config import settings


class DatabaseProvider:
    engine = create_async_engine(
        settings.DB_URL, echo=settings.DB_VERBOSE, future=True
    )

    async_session_factory = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    @staticmethod
    async def get_db() -> AsyncGenerator[AsyncSession, None]:
        """
        Dependency to provide an AsyncSession for FastAPI endpoints.
        Automatically handles session lifecycle.
        """
        async with DatabaseProvider.async_session_factory() as session:
            try:
                yield session
            finally:
                await session.close()
