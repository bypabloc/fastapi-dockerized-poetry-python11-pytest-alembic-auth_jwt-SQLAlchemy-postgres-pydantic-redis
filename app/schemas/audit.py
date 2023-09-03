"""
Audit schemas

Path: app/schemas/audit.py
"""
from datetime import datetime
from pydantic import BaseModel, UUID4


class AuditBase(BaseModel):
    """
    Audit base schema

    :Attributes
        - user_id: UUID4
        - project_id: UUID4
        - task_id: UUID4
        - action: str
        - description: str
    """
    user_id: UUID4
    project_id: UUID4
    task_id: UUID4
    action: str
    description: str


class AuditCreate(AuditBase):
    """
    Audit create schema

    :Attributes
        - user_id: UUID4
        - project_id: UUID4
        - task_id: UUID4
        - action: str
        - description: str
    """
    pass


class AuditUpdate(AuditBase):
    """
    Audit update schema

    :Attributes
        - description: str
    """
    pass


class AuditSchema(AuditBase):
    """
    Audit schema

    :Attributes
        - id: UUID4
        - is_active: bool
        - created_at: datetime
        - updated_at: datetime
    """
    id: UUID4
    is_active: bool
    created_at: datetime
    updated_at: datetime = None

    class Config:
        """
        Pydantic config
        """
        from_attributes = True
