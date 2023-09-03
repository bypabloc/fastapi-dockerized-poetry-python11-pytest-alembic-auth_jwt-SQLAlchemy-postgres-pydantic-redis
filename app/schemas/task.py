"""
Task schemas

Path: app/schemas/task.py
"""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, UUID4


class TaskBase(BaseModel):
    """
    Task base schema

    :Attributes
        - name: str
        - description: str
        - due_date: datetime
        - priority: int
    """
    name: str
    description: str = None
    due_date: datetime = None
    priority: int = None


class TaskCreate(TaskBase):
    """
    Task create schema

    :Attributes
        - name: str
        - description: str
        - due_date: datetime
        - priority: int
    """
    pass


class TaskUpdate(TaskBase):
    """
    Task update schema

    :Attributes
        - name: str
        - description: str
        - due_date: datetime
        - priority: int
    """
    pass


class TaskSchema(TaskBase):
    """
    Task schema

    :Attributes
        - id: UUID4
        - is_active: bool
        - created_at: datetime
        - updated_at: datetime
        - parent_id: UUID4
        - project_id: UUID4
    """
    id: UUID4
    is_active: bool
    created_at: datetime
    updated_at: datetime = None
    parent_id: UUID4 = None
    project_id: UUID4

    class Config:
        """
        Pydantic config
        """
        from_attributes = True
