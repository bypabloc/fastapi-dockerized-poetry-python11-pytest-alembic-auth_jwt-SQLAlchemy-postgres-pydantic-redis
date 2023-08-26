from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import Column, DateTime, String
from sqlalchemy.sql import expression as sql
from sqlalchemy.ext.declarative import declared_attr


from app.utils.logger import CustomLogger
from app.db.main import Base as DBBase

logger = CustomLogger(__name__)


class Base(DBBase):
    """
    User model
    """
    __abstract__ = True  # Esto indica que la clase Base es abstracta y no se debe crear una tabla para ella

    id = Column(String, primary_key=True, default=str(uuid4()))
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, index=True, default=datetime.utcnow)
    updated_at = Column(DateTime, index=True, default=datetime.utcnow)

    @declared_attr
    def __tablename__(self):
        # Generate tablename automatically
        logger.debug(f"Generating tablename for {self.__name__.lower()}")
        return self.__name__.lower()

    def __repr__(self):
        # Generate str representation
        # Get all columns names dynamically
        columns = [c.name for c in self.__table__.columns]
        return (
            f"<{self.__class__.__name__.lower()}("
            f"{', '.join([f'{c}={getattr(self, c)}' for c in columns])}"
            f")>"
        )

    @classmethod
    async def create(cls, **kwargs):
        """Create a new user"""
        raise NotImplementedError

    @classmethod
    async def update(cls, **kwargs):
        """Update a user"""
        raise NotImplementedError

    @classmethod
    async def get(cls, **kwargs):
        """Get a user"""
        raise NotImplementedError

    @classmethod
    async def get_all(cls, **kwargs):
        """Get all users"""
        raise NotImplementedError

    @classmethod
    async def delete(*args, **kwargs):
        """Delete a user"""
        raise NotImplementedError
