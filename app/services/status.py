from sqlalchemy.orm import Session
from app.models.status import Status
from app.schemas.status import StatusCreate, StatusUpdate
from app.utils.logger import CustomLogger
from typing import List, Optional

logger = CustomLogger(__name__)

class StatusService:
    @staticmethod
    async def create_status(db: Session, status_data: StatusCreate) -> Status:
        """
        Crea un nuevo estado
        """
        new_status = Status(**status_data.dict())
        db.add(new_status)
        await db.commit()
        await db.refresh(new_status)
        return new_status

    @staticmethod
    async def update_status(db: Session, status_id: str, update_data: StatusUpdate) -> Status:
        """
        Actualiza un estado existente
        """
        status = await db.query(Status).filter(Status.id == status_id).first()
        if not status:
            return None
        for key, value in update_data.dict().items():
            setattr(status, key, value)
        await db.commit()
        await db.refresh(status)
        return status

    @staticmethod
    async def delete_status(db: Session, status_id: str) -> bool:
        """
        Elimina un estado (soft delete)
        """
        status = await db.query(Status).filter(Status.id == status_id).first()
        if not status:
            return False
        status.is_active = False
        await db.commit()
        return True

    @staticmethod
    async def get_status_by_id(db: Session, status_id: str) -> Optional[Status]:
        """
        Obtiene un estado por su ID
        """
        return await db.query(Status).filter(Status.id == status_id).first()

    @staticmethod
    async def list_statuses(db: Session, project_id: str, skip: int = 0, limit: int = 100) -> List[Status]:
        """
        Lista todos los estados de un proyecto
        """
        return await db.query(Status).filter(Status.project_id == project_id).offset(skip).limit(limit).all()
