"""
UserRole schemas

Path: app/schemas/user_role.py
"""
from datetime import datetime
from pydantic import BaseModel, UUID4


class UserRoleBase(BaseModel):
    """
    UserRole base schema

    :Attributes
        - user_id: UUID4
        - role_id: UUID4
    """
    user_id: UUID4
    role_id: UUID4


class UserRoleCreate(UserRoleBase):
    """
    UserRole create schema

    :Attributes
        - user_id: UUID4
        - role_id: UUID4
    """
    pass


class UserRoleUpdate(UserRoleBase):
    """
    UserRole update schema

    :Attributes
        - user_id: UUID4
        - role_id: UUID4
    """
    pass


class UserRoleSchema(UserRoleBase):
    """
    UserRole schema

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
