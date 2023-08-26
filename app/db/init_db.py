from app.db.base_class import Base
from app.db.main import engine
from app.db.main import SessionLocal
from app.config.setting import settings
from app.schemas.user import UserCreate


def init_db() -> None:
    """
    Initialize database
    """
    database = SessionLocal()

    Base.metadata.create_all(bind=engine)

    user = get_user_by_email(database, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = user.create(database, obj_in=user_in)
