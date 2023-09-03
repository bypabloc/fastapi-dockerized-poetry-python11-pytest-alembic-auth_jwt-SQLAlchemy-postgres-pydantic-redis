"""
Status schemas

Path: app/schemas/status.py
"""
from datetime import datetime
from pydantic import BaseModel, UUID4, Field


class StatusBase(BaseModel):
    """
    Status base schema

    :Attributes
        - name: str
        - color: str
        - order: int
    """
    name: str
    color: str
    order: int


class StatusCreate(StatusBase):
    """
    Status create schema

    :Attributes
        - name: str
        - color: str
        - order: int
    """
    pass


class StatusUpdate(StatusBase):
    """
    Status update schema

    :Attributes
        - name: str
        - color: str
        - order: int
    """
    pass


class StatusSchema(StatusBase):
    """
    Status schema

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
