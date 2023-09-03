from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.utils.security import get_password_hash
from app.utils.logger import CustomLogger
from typing import List

logger = CustomLogger(__name__)


class UserService:
    @staticmethod
    async def create_user(db: Session, user_data: UserCreate) -> User:
        """
        Crea un nuevo usuario
        """
        hashed_password = get_password_hash(user_data.password)
        new_user = User(email=user_data.email, hashed_password=hashed_password)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user

    @staticmethod
    async def update_user(db: Session, user_id: str, update_data: UserUpdate) -> User:
        """
        Actualiza un usuario existente
        """
        user = await db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        for key, value in update_data.dict().items():
            setattr(user, key, value)
        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def delete_user(db: Session, user_id: str) -> bool:
        """
        Elimina un usuario (soft delete)
        """
        user = await db.query(User).filter(User.id == user_id).first()
        if not user:
            return False
        user.is_active = False
        await db.commit()
        return True

    @staticmethod
    async def get_user_by_email(db: Session, email: str) -> User:
        """
        Obtiene un usuario por su correo electrónico
        """
        return await db.query(User).filter(User.email == email).first()

    @staticmethod
    async def get_all_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        """
        Obtiene todos los usuarios
        """
        return await db.query(User).offset(skip).limit(limit).all()
