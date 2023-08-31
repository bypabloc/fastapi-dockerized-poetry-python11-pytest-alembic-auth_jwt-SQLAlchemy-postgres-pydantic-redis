"""
User schemas

Path: app/schemas/user.py
"""

from datetime import datetime
from pydantic import BaseModel, UUID4



class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserSchema(UserBase):
    id: UUID4
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class UserUpdate(UserBase):
    password: str
