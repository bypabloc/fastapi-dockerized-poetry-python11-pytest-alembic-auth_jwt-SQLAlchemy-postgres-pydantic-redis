"""
Base model

This module contains the base model for all models in the application.

The base model is used to store the common attributes and methods for all models.

Path: app/models/base.py
"""

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
        name_class = self.__name__.lower()
        logger.debug(f"Generating tablename for {name_class}")
        name_class = f'{name_class}s'
        return name_class

    def __repr__(self):
        # Generate str representation
        # Get all columns names dynamically
        columns = [c.name for c in self.__table__.columns]
        return (
            f"<{self.__class__.__name__.lower()}("
            f"{', '.join([f'{c}={getattr(self, c)}' for c in columns])}"
            f")>"
        )
