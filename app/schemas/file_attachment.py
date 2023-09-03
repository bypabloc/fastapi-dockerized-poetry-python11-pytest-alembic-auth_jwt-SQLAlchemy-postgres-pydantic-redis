"""
FileAttachment schemas

Path: app/schemas/file_attachment.py
"""
from datetime import datetime
from pydantic import BaseModel, UUID4
from typing import Union


class FileAttachmentBase(BaseModel):
    """
    FileAttachment base schema

    :Attributes
        - task_id: UUID4
        - project_id: UUID4
        - file_path: str
    """
    task_id: Union[UUID4, None]
    project_id: Union[UUID4, None]
    file_path: str


class FileAttachmentCreate(FileAttachmentBase):
    """
    FileAttachment create schema

    :Attributes
        - task_id: UUID4
        - project_id: UUID4
        - file_path: str
    """
    pass


class FileAttachmentUpdate(FileAttachmentBase):
    """
    FileAttachment update schema

    :Attributes
        - file_path: str
    """
    pass


class FileAttachmentSchema(FileAttachmentBase):
    """
    FileAttachment schema

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
