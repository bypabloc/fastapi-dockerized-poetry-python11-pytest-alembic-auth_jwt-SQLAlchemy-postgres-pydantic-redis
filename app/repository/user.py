from app.repository.base import RepositoryBase

from app.models.user import User
from app.schemas.user import UserSchema
from app.schemas.user import UserCreate
from app.schemas.user import UserUpdate

from app.utils.security import get_password_hash
from app.utils.logger import CustomLogger

logger = CustomLogger(__name__)


class UserRepository(RepositoryBase):
    """
    User repository
    """
    async def create(self, obj_in: UserCreate) -> UserSchema:
        """
        Create a new user
        """
        obj = obj_in.dict()
        hashed_password = get_password_hash(obj.pop("password"))
        logger.info(f"hashed_password: {hashed_password}")
        obj["hashed_password"] = hashed_password
        user = await User.create(
            database=self.database,
            **obj,
        )
        return user

    def update(self, idx: str, obj_in: UserUpdate) -> UserSchema:
        """
        Update a user
        """
        obj = obj_in.dict()
        if obj.get("password"):
            obj["hashed_password"] = get_password_hash(obj.pop("password"))
        return User.update(
            database=self.database,
            idx=idx,
            **obj,
        )

    def delete(self, idx: str) -> UserSchema:
        """
        Delete a user
        """
        return User.delete(
            database=self.database,
            idx=idx,
            soft_delete=True,
        )

    def get(self, idx: str) -> UserSchema:
        """
        Get a user
        """
        return User.get(
            database=self.database,
            idx=idx,
        )

    async def get_all(self, skip: int = 0, limit: int = 100) -> list[UserSchema]:
        """
        Get all users
        """
        users = await User.get_all(
            database=self.database,
            skip=skip,
            limit=limit,
        )
        return [UserSchema.from_orm(user) for user in users]

    async def get_by_email(self, email: str) -> UserSchema:
        """
        Get a user by email
        """
        user = await User.get_by_email(
            database=self.database,
            email=email,
        )
        if not user:
            return None
        return user
