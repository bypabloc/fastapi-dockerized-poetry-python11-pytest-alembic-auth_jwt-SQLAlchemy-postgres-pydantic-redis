# app/models/project.py

from sqlalchemy import Column, String, ForeignKey, Integer, Boolean, DateTime, Text
from app.models.base import Base


class Project(Base):
    __tablename__ = 'projects'

    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    is_public = Column(Boolean, nullable=False)
    owner_id = Column(String, ForeignKey('users.id'))
