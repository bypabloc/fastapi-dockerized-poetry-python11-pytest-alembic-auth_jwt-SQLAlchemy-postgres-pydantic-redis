from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.utils.logger import CustomLogger
from typing import List, Optional

logger = CustomLogger(__name__)


class ProjectService:
    @staticmethod
    async def create_project(db: Session, project_data: ProjectCreate) -> Project:
        """
        Crea un nuevo proyecto
        """
        new_project = Project(**project_data.dict())
        db.add(new_project)
        await db.commit()
        await db.refresh(new_project)
        return new_project

    @staticmethod
    async def update_project(db: Session, project_id: str, update_data: ProjectUpdate) -> Project:
        """
        Actualiza un proyecto existente
        """
        project = await db.query(Project).filter(Project.id == project_id).first()
        if not project:
            return None
        for key, value in update_data.dict().items():
            setattr(project, key, value)
        await db.commit()
        await db.refresh(project)
        return project

    @staticmethod
    async def delete_project(db: Session, project_id: str) -> bool:
        """
        Elimina un proyecto (soft delete)
        """
        project = await db.query(Project).filter(Project.id == project_id).first()
        if not project:
            return False
        project.is_active = False
        await db.commit()
        return True

    @staticmethod
    async def get_project_by_id(db: Session, project_id: str) -> Optional[Project]:
        """
        Obtiene un proyecto por su ID
        """
        return await db.query(Project).filter(Project.id == project_id).first()

    @staticmethod
    async def list_projects(db: Session, user_id: str, skip: int = 0, limit: int = 100) -> List[Project]:
        """
        Lista todos los proyectos de un usuario
        """
        return await db.query(Project).filter(Project.user_id == user_id).offset(skip).limit(limit).all()
