from sqlalchemy.orm import Session
from app.models.audit import Audit
from app.schemas.audit import AuditCreate
from app.utils.logger import CustomLogger
from typing import List, Optional

logger = CustomLogger(__name__)

class AuditService:
    @staticmethod
    async def create_audit_record(db: Session, audit_data: AuditCreate) -> Audit:
        """
        Crea un nuevo registro de auditoría
        """
        new_audit_record = Audit(**audit_data.dict())
        db.add(new_audit_record)
        await db.commit()
        await db.refresh(new_audit_record)
        return new_audit_record

    @staticmethod
    async def get_audit_by_id(db: Session, audit_id: str) -> Optional[Audit]:
        """
        Obtiene un registro de auditoría por su ID
        """
        return await db.query(Audit).filter(Audit.id == audit_id).first()

    @staticmethod
    async def list_audit_records(db: Session, parent_id: str, skip: int = 0, limit: int = 100) -> List[Audit]:
        """
        Lista todos los registros de auditoría para un proyecto o tarea específica
        """
        return await db.query(Audit).filter(Audit.parent_id == parent_id).offset(skip).limit(limit).all()
