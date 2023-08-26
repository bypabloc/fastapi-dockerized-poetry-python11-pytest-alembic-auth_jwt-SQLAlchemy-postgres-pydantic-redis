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
    def __init__(self):
        """
        Constructor
        """
        self.__session = None
        self.__engine = None

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
        )

    async def disconnect(self):
        """
        Disconnect from database
        """
        await self.__engine.dispose()

    async def get_db(self):
        """
        Get database
        """
        async with db.__session() as session:
            yield session


db = Database()
