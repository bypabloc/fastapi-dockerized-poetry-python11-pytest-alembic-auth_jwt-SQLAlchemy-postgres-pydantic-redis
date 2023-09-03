"""
UserProject schemas

Path: app/schemas/user_project.py
"""
from datetime import datetime
from pydantic import BaseModel, UUID4


class UserProjectBase(BaseModel):
    """
    UserProject base schema

    :Attributes
        - user_id: UUID4
        - project_id: UUID4
    """
    user_id: UUID4
    project_id: UUID4


class UserProjectCreate(UserProjectBase):
    """
    UserProject create schema

    :Attributes
        - user_id: UUID4
        - project_id: UUID4
    """
    pass


class UserProjectUpdate(UserProjectBase):
    """
    UserProject update schema

    :Attributes
        - user_id: UUID4
        - project_id: UUID4
    """
    pass


class UserProjectSchema(UserProjectBase):
    """
    UserProject schema

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
