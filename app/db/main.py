"""
Database module

Path: app/db/main.py
"""

from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from app.config.database import settings_database as settings
from app.utils.logger import CustomLogger


logger = CustomLogger(__name__)


Base = declarative_base()


class Database:
    """
    Database class
    """
    def __init__(self, db_uri: str):
        """
        Constructor
        """
        logger.info(f"DB_URI: {db_uri}")
        self.__engine = create_async_engine(db_uri)
        self.__session = async_sessionmaker(
            bind=self.__engine,
            expire_on_commit=False,
            class_=AsyncSession,
        )

    def connect(self):
        """
        Connect to database
        """
        self.__engine = create_async_engine(
            settings.DB_URI,
        )

        self.__session = async_sessionmaker(
            bind=self.__engine,
            autocommit=False,
            autoflush=True,
        )

    async def disconnect(self):
        """
        Disconnect from database
        """
        await self.__engine.dispose()

    @asynccontextmanager
    async def get_db(self):
        """
        Get database
        """
        session = self.__session()
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
        finally:
            await session.close()
