from typing import Generator

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from jwt import encode as jwt_encode
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.models.user import User


# from app.schemas.item import ItemCreate
# from app.schemas.token import TokenPayload

from app.config.setting import settings
from app.db.main import Database
from app.config.database import settings_database
from app.utils.logger import CustomLogger


logger = CustomLogger(__name__)
DB_URI = settings_database.DB_URI
db = Database(DB_URI)
ALGORITHM = settings.ALGORITHM


# reusable_oauth2 = OAuth2PasswordBearer(
#     tokenUrl=f"{settings.API_V1_STR}/login/access-token"
# )

async def get_db():
    """
    Dependency to get database connection.
    """
    async with db.get_db() as session:
        return session


# def get_current_user(
#     database: Session = Depends(db.get_db()),
#     token: str = Depends(reusable_oauth2),
# ) -> User:
#     try:
#         payload = jwt_encode(
#             token,
#             settings.SECRET_KEY,
#             algorithms=[SECURITY_ALGORITHM],
#         )
#         token_data = TokenPayload(**payload)
#     except (ValidationError, ValueError):
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Could not validate credentials",
#         )
#     user = get_user(database, id=token_data.sub)
#     if not user:
#         raise HTTPException(
#             status_code=404,
#             detail="User not found",
#         )
#     return user


# def get_current_active_user(
#     current_user: User = Depends(get_current_user),
# ) -> User:
#     if not is_user_active(current_user):
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


# def get_current_active_superuser(
#     current_user: User = Depends(get_current_user),
# ) -> User:
#     if not is_user_superuser(current_user):
#         raise HTTPException(
#             status_code=400, detail="The user doesn't have enough privileges"
#         )
#     return current_user
