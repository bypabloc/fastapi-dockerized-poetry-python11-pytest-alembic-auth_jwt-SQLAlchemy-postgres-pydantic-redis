# app/models/audit_log.py

from sqlalchemy import Column, String, ForeignKey, Integer, Boolean, DateTime, Text
from app.models.base import Base


class AuditLog(Base):
    __tablename__ = 'audit_log'

    user_id = Column(String, ForeignKey('users.id'))
    action = Column(String, nullable=False)
    entity_type = Column(String, nullable=False)
    entity_id = Column(String, nullable=False)
    changed_fields = Column(Text, nullable=True)
