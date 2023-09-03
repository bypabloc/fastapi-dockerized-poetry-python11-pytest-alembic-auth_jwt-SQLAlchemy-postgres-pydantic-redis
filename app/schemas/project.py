"""
Project schemas

Path: app/schemas/project.py
"""
from datetime import datetime
from typing import List
from pydantic import BaseModel, UUID4


class ProjectBase(BaseModel):
    """
    Project base schema

    :Attributes
        - name: str
        - description: str
        - is_public: bool
        - is_multi_tenancy: bool
    """
    name: str
    description: str = None
    is_public: bool = True
    is_multi_tenancy: bool = False


class ProjectCreate(ProjectBase):
    """
    Project create schema

    :Attributes
        - name: str
        - description: str
        - is_public: bool
        - is_multi_tenancy: bool
    """
    pass


class ProjectUpdate(ProjectBase):
    """
    Project update schema

    :Attributes
        - name: str
        - description: str
        - is_public: bool
        - is_multi_tenancy: bool
    """
    pass


class ProjectSchema(ProjectBase):
    """
    Project schema

    :Attributes
        - id: UUID4
        - is_active: bool
        - created_at: datetime
        - updated_at: datetime
        - owner_id: UUID4
    """
    id: UUID4
    is_active: bool
    created_at: datetime
    updated_at: datetime = None
    owner_id: UUID4

    class Config:
        """
        Pydantic config
        """
        from_attributes = True
