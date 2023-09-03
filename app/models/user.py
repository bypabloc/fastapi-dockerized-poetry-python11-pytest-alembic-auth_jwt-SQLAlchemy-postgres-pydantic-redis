"""
User model

This model is used to store the user information

Path: app/models/user.py
"""

from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey, Integer, Boolean, DateTime, Text
from sqlalchemy.sql import expression as sql

from app.models.base import Base
from app.utils.logger import CustomLogger

logger = CustomLogger(__name__)


class User(Base):
    """
    User model
    """
    __tablename__ = 'users'

    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    profile_image_url = Column(String, nullable=True)
    google_id = Column(String, nullable=True)
    facebook_id = Column(String, nullable=True)
    github_id = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    bio = Column(Text, nullable=True)
    location = Column(String, nullable=True)
    website = Column(String, nullable=True)
    date_of_birth = Column(DateTime, nullable=True)
    language = Column(String, nullable=True)
    timezone = Column(String, nullable=True)
    notifications_enabled = Column(Boolean, default=False)

    @classmethod
    async def create(cls, database, **kwargs) -> "User":
        """Create a new user"""
        logger.info(f"database: {database}")
        query = (
            sql.insert(cls)
            .values(
                id=str(uuid4()),
                **kwargs
            )
            .returning(
                cls.id,
                cls.email
            )
        )
        users = await database.execute(query)
        await database.commit()
        return users.first()

    @classmethod
    async def get_all(cls, database, skip: int = 0, limit: int = 100) -> list["User"]:
        """
        Get all users

        :param database: Database session
        :param kwargs: can contain skip and limit

        :return: List of users
        """
        logger.info(f"database: {database}")
        logger.info(f"type(database): {type(database)}")
        logger.info(f"dir(database): {dir(database)}")
        query = sql.select(cls).offset(skip).limit(limit).order_by(cls.created_at.desc())
        result = await database.execute(query)
        users = result.scalars().all()
        logger.info(f"users: {users}")
        return users

    @classmethod
    async def get_by_email(cls, database, email) -> "User":
        """Get a user by email"""
        query = sql.select(cls).where(cls.email == email)
        users = await database.execute(query)
        user = users.first()  # No desempaquetes aquí
        if user is None:
            return None
        return user  # Retorna el usuario o None si no se encuentra
