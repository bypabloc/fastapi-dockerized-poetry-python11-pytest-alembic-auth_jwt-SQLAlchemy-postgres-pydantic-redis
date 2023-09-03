from sqlalchemy.orm import Session
from app.models.label import Label
from app.schemas.label import LabelCreate, LabelUpdate
from app.utils.logger import CustomLogger
from typing import List, Optional

logger = CustomLogger(__name__)

class LabelService:
    @staticmethod
    async def create_label(db: Session, label_data: LabelCreate) -> Label:
        """
        Crea una nueva etiqueta
        """
        new_label = Label(**label_data.dict())
        db.add(new_label)
        await db.commit()
        await db.refresh(new_label)
        return new_label

    @staticmethod
    async def update_label(db: Session, label_id: str, update_data: LabelUpdate) -> Label:
        """
        Actualiza una etiqueta existente
        """
        label = await db.query(Label).filter(Label.id == label_id).first()
        if not label:
            return None
        for key, value in update_data.dict().items():
            setattr(label, key, value)
        await db.commit()
        await db.refresh(label)
        return label

    @staticmethod
    async def delete_label(db: Session, label_id: str) -> bool:
        """
        Elimina una etiqueta (soft delete)
        """
        label = await db.query(Label).filter(Label.id == label_id).first()
        if not label:
            return False
        label.is_active = False
        await db.commit()
        return True

    @staticmethod
    async def get_label_by_id(db: Session, label_id: str) -> Optional[Label]:
        """
        Obtiene una etiqueta por su ID
        """
        return await db.query(Label).filter(Label.id == label_id).first()

    @staticmethod
    async def list_labels(db: Session, project_id: str, skip: int = 0, limit: int = 100) -> List[Label]:
        """
        Lista todas las etiquetas de un proyecto
        """
        return await db.query(Label).filter(Label.project_id == project_id).offset(skip).limit(limit).all()
