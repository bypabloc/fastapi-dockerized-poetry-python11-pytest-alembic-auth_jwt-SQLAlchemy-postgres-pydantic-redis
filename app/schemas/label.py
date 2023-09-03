"""
Label schemas

Path: app/schemas/label.py
"""
from datetime import datetime
from pydantic import BaseModel, UUID4, Field


class LabelBase(BaseModel):
    """
    Label base schema

    :Attributes
        - name: str
        - color: str
    """
    name: str
    color: str


class LabelCreate(LabelBase):
    """
    Label create schema

    :Attributes
        - name: str
        - color: str
    """
    pass


class LabelUpdate(LabelBase):
    """
    Label update schema

    :Attributes
        - name: str
        - color: str
    """
    pass


class LabelSchema(LabelBase):
    """
    Label schema

    :Attributes
        - id: UUID4
        - is_active: bool
        - is_visible: bool
        - created_at: datetime
        - updated_at: datetime
    """
    id: UUID4
    is_active: bool
    is_visible: bool = Field(..., alias='visibility')
    created_at: datetime
    updated_at: datetime = None

    class Config:
        """
        Pydantic config
        """
        from_attributes = True
