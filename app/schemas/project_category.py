"""
ProjectCategory schemas

Path: app/schemas/project_category.py
"""
from datetime import datetime
from pydantic import BaseModel, UUID4


class ProjectCategoryBase(BaseModel):
    """
    ProjectCategory base schema

    :Attributes
        - name: str
        - description: str
    """
    name: str
    description: str


class ProjectCategoryCreate(ProjectCategoryBase):
    """
    ProjectCategory create schema

    :Attributes
        - name: str
        - description: str
    """
    pass


class ProjectCategoryUpdate(ProjectCategoryBase):
    """
    ProjectCategory update schema

    :Attributes
        - name: str
        - description: str
    """
    pass


class ProjectCategorySchema(ProjectCategoryBase):
    """
    ProjectCategory schema

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
