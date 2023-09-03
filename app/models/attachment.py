# app/models/attachment.py

from sqlalchemy import Column, String, ForeignKey, Integer, Boolean, DateTime, Text
from app.models.base import Base


class Attachment(Base):
    __tablename__ = 'attachments'

    file_path = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    task_id = Column(String, ForeignKey('tasks.id'), nullable=True)
    project_id = Column(String, ForeignKey('projects.id'), nullable=True)
