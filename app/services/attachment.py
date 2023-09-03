from sqlalchemy.orm import Session
from app.models.attachment import Attachment
from app.schemas.attachment import AttachmentCreate, AttachmentUpdate
from app.utils.logger import CustomLogger
from typing import List, Optional

logger = CustomLogger(__name__)

class AttachmentService:
    @staticmethod
    async def create_attachment(db: Session, attachment_data: AttachmentCreate) -> Attachment:
        """
        Crea un nuevo archivo adjunto
        """
        new_attachment = Attachment(**attachment_data.dict())
        db.add(new_attachment)
        await db.commit()
        await db.refresh(new_attachment)
        return new_attachment

    @staticmethod
    async def update_attachment(db: Session, attachment_id: str, update_data: AttachmentUpdate) -> Attachment:
        """
        Actualiza un archivo adjunto existente
        """
        attachment = await db.query(Attachment).filter(Attachment.id == attachment_id).first()
        if not attachment:
            return None
        for key, value in update_data.dict().items():
            setattr(attachment, key, value)
        await db.commit()
        await db.refresh(attachment)
        return attachment

    @staticmethod
    async def delete_attachment(db: Session, attachment_id: str) -> bool:
        """
        Elimina un archivo adjunto (soft delete)
        """
        attachment = await db.query(Attachment).filter(Attachment.id == attachment_id).first()
        if not attachment:
            return False
        attachment.is_active = False
        await db.commit()
        return True

    @staticmethod
    async def get_attachment_by_id(db: Session, attachment_id: str) -> Optional[Attachment]:
        """
        Obtiene un archivo adjunto por su ID
        """
        return await db.query(Attachment).filter(Attachment.id == attachment_id).first()

    @staticmethod
    async def list_attachments(db: Session, parent_id: str, skip: int = 0, limit: int = 100) -> List[Attachment]:
        """
        Lista todos los archivos adjuntos de un proyecto o tarea
        """
        return await db.query(Attachment).filter(Attachment.parent_id == parent_id).offset(skip).limit(limit).all()
