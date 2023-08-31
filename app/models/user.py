"""
User model

This model is used to store the user information

Path: app/models/user.py
"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import Column, DateTime, String
from sqlalchemy.sql import expression as sql


from app.models.base import Base
from app.utils.logger import CustomLogger

logger = CustomLogger(__name__)


class User(Base):
    """
    User model
    """
    # Esta línea establece la clave foránea que apunta a la tabla base
    # id = Column(String, ForeignKey('base.id'), primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

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
    async def update(cls, database, idx, **kwargs) -> "User":
        """Update a user"""
        query = (
            sql.update(cls)
            .where(cls.id == idx)
            .values(**kwargs)
            .execution_options(synchronize_session="fetch")
            .returning(cls.id, cls.email)
        )
        users = await database.execute(query)
        await database.commit()
        return users.first()

    @classmethod
    async def get(cls, database, idx) -> "User":
        """Get a user"""
        query = sql.select(cls).where(cls.id == idx)
        users = await database.execute(query)
        (user,) = users.first()
        return user

    @classmethod
    async def delete(cls, database, idx) -> bool:
        """Delete a user"""
        query = (
            sql.delete(cls)
            .where(cls.id == idx)
            .returning(
                cls.id,
                cls.email,
            )
        )
        await database.execute(query)
        await database.commit()
        return True

    @classmethod
    async def get_by_email(cls, database, email) -> "User":
        """Get a user by email"""
        query = sql.select(cls).where(cls.email == email)
        users = await database.execute(query)
        user = users.first()  # No desempaquetes aquí
        if user is None:
            return None
        return user  # Retorna el usuario o None si no se encuentra
