"""
User endpoints.

This file contains the endpoints for the user model.

Path: app/api/v1/endpoints/user.py
"""

from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.utils.logger import CustomLogger
from app.repository.user import UserRepository
from app.api.deps import get_db


logger = CustomLogger(__name__)

router = APIRouter()


@router.get(
    "/",
    # response_model=List[UserSchema],
)
async def read_users(
    session: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    # current_user: User = Depends(get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    user_repo = UserRepository(database=session)
    users = await user_repo.get_all(skip=skip, limit=limit)
    return users
