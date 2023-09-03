# app/models/category.py

from sqlalchemy import Column, String, ForeignKey, Integer, Boolean, DateTime, Text
from app.models.base import Base


class Category(Base):
    __tablename__ = 'categories'

    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
