"""
User schemas

Path: app/schemas/user.py
"""
from datetime import datetime
from pydantic import BaseModel, UUID4, EmailStr


class UserBase(BaseModel):
    """
    User base schema

    :Attributes
        - email: EmailStr
        - profile_image: str (URL)
        - google_id: str
        - facebook_id: str
        - github_id: str
    """
    email: EmailStr
    profile_image: str = None
    google_id: str = None
    facebook_id: str = None
    github_id: str = None


class UserCreate(UserBase):
    """
    User create schema

    :Attributes
        - email: EmailStr
        - password: str
        - profile_image: str
        - google_id: str
        - facebook_id: str
        - github_id: str
    """
    password: str


class UserUpdate(UserBase):
    """
    User update schema

    :Attributes
        - password: str
    """
    password: str = None


class UserProfile(UserBase):
    """
    User profile schema

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


class UserSchema(UserProfile):
    """
    User schema with hashed password (For internal use)

    :Attributes
        - hashed_password: str
    """
    hashed_password: str
