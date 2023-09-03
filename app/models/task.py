from sqlalchemy import Column, String, ForeignKey, Integer, Boolean, DateTime, Text
from app.models.base import Base


class Task(Base):
    __tablename__ = 'tasks'

    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    status_id = Column(String, ForeignKey('statuses.id'))
    project_id = Column(String, ForeignKey('projects.id'))
    parent_id = Column(String, ForeignKey('tasks.id'), nullable=True)
    priority = Column(Integer, nullable=True)
    due_date = Column(DateTime, nullable=True)