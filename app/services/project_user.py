from sqlalchemy.orm import Session
from app.models.project_user import ProjectUser
from app.schemas.project_user import ProjectUserCreate, ProjectUserUpdate
from app.utils.logger import CustomLogger
from typing import List, Optional

logger = CustomLogger(__name__)

class ProjectUserService:
    @staticmethod
    async def add_user_to_project(db: Session, user_data: ProjectUserCreate) -> ProjectUser:
        """
        Agrega un usuario a un proyecto y le asigna un rol
        """
        new_project_user = ProjectUser(**user_data.dict())
        db.add(new_project_user)
        await db.commit()
        await db.refresh(new_project_user)
        return new_project_user

    @staticmethod
    async def update_project_user(db: Session, project_user_id: str, update_data: ProjectUserUpdate) -> ProjectUser:
        """
        Actualiza el rol o estado de un usuario en un proyecto
        """
        project_user = await db.query(ProjectUser).filter(ProjectUser.id == project_user_id).first()
        if not project_user:
            return None
        for key, value in update_data.dict().items():
            setattr(project_user, key, value)
        await db.commit()
        await db.refresh(project_user)
        return project_user

    @staticmethod
    async def remove_user_from_project(db: Session, project_user_id: str) -> bool:
        """
        Elimina un usuario de un proyecto (soft delete)
        """
        project_user = await db.query(ProjectUser).filter(ProjectUser.id == project_user_id).first()
        if not project_user:
            return False
        project_user.is_active = False
        await db.commit()
        return True

    @staticmethod
    async def get_project_user_by_id(db: Session, project_user_id: str) -> Optional[ProjectUser]:
        """
        Obtiene la información de un usuario en un proyecto específico
        """
        return await db.query(ProjectUser).filter(ProjectUser.id == project_user_id).first()

    @staticmethod
    async def list_project_users(db: Session, project_id: str, skip: int = 0, limit: int = 100) -> List[ProjectUser]:
        """
        Lista todos los usuarios de un proyecto
        """
        return await db.query(ProjectUser).filter(ProjectUser.project_id == project_id).offset(skip).limit(limit).all()
