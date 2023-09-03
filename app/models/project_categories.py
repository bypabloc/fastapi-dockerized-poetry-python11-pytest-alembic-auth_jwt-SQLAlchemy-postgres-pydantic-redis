# app/models/project_categories.py

from sqlalchemy import Column, String, ForeignKey, Integer, Boolean, DateTime, Text
from app.models.base import Base


class ProjectCategory(Base):
    __tablename__ = 'project_categories'

    project_id = Column(String, ForeignKey('projects.id'))
    category_id = Column(String, ForeignKey('categories.id'))
