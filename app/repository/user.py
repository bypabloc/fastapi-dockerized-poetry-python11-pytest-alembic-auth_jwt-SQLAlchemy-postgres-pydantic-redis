from app.repository.base import RepositoryBase

from app.models.user import User
from app.schemas.user import UserSchema
from app.schemas.user import UserCreate
from app.schemas.user import UserUpdate

from app.utils.security import get_password_hash


class UserRepository(RepositoryBase):
    """
    User repository
    """
    model = User
    schema = UserSchema

    def create(self, obj_in: UserCreate) -> UserSchema:
        """
        Create a new user
        """
        obj = obj_in.dict()
        obj["hashed_password"] = get_password_hash(obj.pop("password"))
        return self.model.create(
            database=self.database,
            **obj,
        )

    def update(self, idx: str, obj_in: UserUpdate) -> UserSchema:
        """
        Update a user
        """
        obj = obj_in.dict()
        if obj.get("password"):
            obj["hashed_password"] = get_password_hash(obj.pop("password"))
        return self.model.update(
            database=self.database,
            idx=idx,
            **obj,
        )

    def delete(self, idx: str) -> UserSchema:
        """
        Delete a user
        """
        return self.model.delete(
            database=self.database,
            idx=idx,
            soft_delete=True,
        )

    def get(self, idx: str) -> UserSchema:
        """
        Get a user
        """
        return self.model.get(
            database=self.database,
            idx=idx,
        )

    async def get_all(self, skip: int = 0, limit: int = 100) -> list[UserSchema]:
        """
        Get all users
        """
        return await self.model.get_all(
            database=self.database,
            skip=skip,
            limit=limit,
        )
