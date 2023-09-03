"""
TaskComment schemas

Path: app/schemas/task_comment.py
"""
from datetime import datetime
from pydantic import BaseModel, UUID4


class TaskCommentBase(BaseModel):
    """
    TaskComment base schema

    :Attributes
        - task_id: UUID4
        - user_id: UUID4
        - comment: str
    """
    task_id: UUID4
    user_id: UUID4
    comment: str


class TaskCommentCreate(TaskCommentBase):
    """
    TaskComment create schema

    :Attributes
        - task_id: UUID4
        - user_id: UUID4
        - comment: str
    """
    pass


class TaskCommentUpdate(TaskCommentBase):
    """
    TaskComment update schema

    :Attributes
        - comment: str
    """
    pass


class TaskCommentSchema(TaskCommentBase):
    """
    TaskComment schema

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
