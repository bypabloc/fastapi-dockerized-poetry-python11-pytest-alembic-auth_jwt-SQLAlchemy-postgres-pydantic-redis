"""
Role schemas

Path: app/schemas/role.py
"""
from datetime import datetime
from pydantic import BaseModel, UUID4


class RoleBase(BaseModel):
    """
    Role base schema

    :Attributes
        - name: str
        - description: str
    """
    name: str
    description: str


class RoleCreate(RoleBase):
    """
    Role create schema

    :Attributes
        - name: str
        - description: str
    """
    pass


class RoleUpdate(RoleBase):
    """
    Role update schema

    :Attributes
        - name: str
        - description: str
    """
    pass


class RoleSchema(RoleBase):
    """
    Role schema

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
