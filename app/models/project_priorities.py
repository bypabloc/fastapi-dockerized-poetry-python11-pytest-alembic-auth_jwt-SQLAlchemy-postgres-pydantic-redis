# app/models/project_priorities.py

from sqlalchemy import Column, String, ForeignKey, Integer, Boolean, DateTime, Text
from app.models.base import Base


class ProjectPriority(Base):
    __tablename__ = 'project_priorities'

    project_id = Column(String, ForeignKey('projects.id'))
    priority_level = Column(Integer, nullable=False)
    display_text = Column(String, nullable=True)
