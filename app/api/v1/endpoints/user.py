from typing import Any
from typing import List

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import HTTPException
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session


# from app.api.deps import get_current_active_superuser
# from app.api.deps import get_current_active_user
from app.db.main import Database
from app.config.database import settings_database
from app.utils.logger import CustomLogger
from app.repository.user import UserRepository


logger = CustomLogger(__name__)
DB_URI = settings_database.DB_URI
db = Database(DB_URI)

router = APIRouter()


@router.get(
    "/",
    # response_model=List[UserSchema],
)
async def read_users(
    database: Session = Depends(db.get_db),
    skip: int = 0,
    limit: int = 100,
    # current_user: User = Depends(get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    users = await UserRepository(database).get_all(skip=skip, limit=limit)
    return users


# @router.post("/", response_model=UserSchema)
# def create_user(
#     *,
#     database: Session = Depends(db.get_db),
#     user_in: UserCreate,
#     # current_user: User = Depends(get_current_active_superuser),
# ) -> Any:
#     """
#     Create new user.
#     """
#     return {}


# @router.put("/me", response_model=UserSchema)
# def update_user_me(
#     *,
#     database: Session = Depends(db.get_db),
#     password: str = Body(None),
#     full_name: str = Body(None),
#     email: EmailStr = Body(None),
#     # current_user: User = Depends(get_current_active_user),
# ) -> Any:
#     """
#     Update own user.
#     """
#     return {}


# @router.get("/me", response_model=UserSchema)
# def read_user_me(
#     database: Session = Depends(db.get_db),
#     # current_user: User = Depends(get_current_active_user),
# ) -> Any:
#     """
#     Get current user.
#     """
#     return {}
