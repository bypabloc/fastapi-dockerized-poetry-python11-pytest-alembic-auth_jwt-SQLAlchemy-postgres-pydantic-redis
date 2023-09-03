"""
Permission schemas

Path: app/schemas/permission.py
"""
from datetime import datetime
from pydantic import BaseModel, UUID4


class PermissionBase(BaseModel):
    """
    Permission base schema

    :Attributes
        - name: str
        - description: str
    """
    name: str
    description: str


class PermissionCreate(PermissionBase):
    """
    Permission create schema

    :Attributes
        - name: str
        - description: str
    """
    pass


class PermissionUpdate(PermissionBase):
    """
    Permission update schema

    :Attributes
        - name: str
        - description: str
    """
    pass


class PermissionSchema(PermissionBase):
    """
    Permission schema

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
