"""
Initialize database

Path: app/db/init_db.py
"""

from app.config.setting import settings
from app.schemas.user import UserCreate
from app.repository.user import UserRepository


async def init_db(database) -> None:
    """
    Initialize database
    """
    user_repository = UserRepository(database)
    user = await user_repository.get_by_email(email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = await user_repository.create(obj_in=user_in)
