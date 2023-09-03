from sqlalchemy.orm import Session
from app.models.role import Role
from app.schemas.role import RoleCreate, RoleUpdate
from app.utils.logger import CustomLogger
from typing import List, Optional

logger = CustomLogger(__name__)

class RoleService:
    @staticmethod
    async def create_role(db: Session, role_data: RoleCreate) -> Role:
        """
        Crea un nuevo rol
        """
        new_role = Role(**role_data.dict())
        db.add(new_role)
        await db.commit()
        await db.refresh(new_role)
        return new_role

    @staticmethod
    async def update_role(db: Session, role_id: str, update_data: RoleUpdate) -> Role:
        """
        Actualiza un rol existente
        """
        role = await db.query(Role).filter(Role.id == role_id).first()
        if not role:
            return None
        for key, value in update_data.dict().items():
            setattr(role, key, value)
        await db.commit()
        await db.refresh(role)
        return role

    @staticmethod
    async def delete_role(db: Session, role_id: str) -> bool:
        """
        Elimina un rol (soft delete)
        """
        role = await db.query(Role).filter(Role.id == role_id).first()
        if not role:
            return False
        role.is_active = False
        await db.commit()
        return True

    @staticmethod
    async def get_role_by_id(db: Session, role_id: str) -> Optional[Role]:
        """
        Obtiene un rol por su ID
        """
        return await db.query(Role).filter(Role.id == role_id).first()

    @staticmethod
    async def list_roles(db: Session, project_id: str, skip: int = 0, limit: int = 100) -> List[Role]:
        """
        Lista todos los roles de un proyecto
        """
        return await db.query(Role).filter(Role.project_id == project_id).offset(skip).limit(limit).all()
