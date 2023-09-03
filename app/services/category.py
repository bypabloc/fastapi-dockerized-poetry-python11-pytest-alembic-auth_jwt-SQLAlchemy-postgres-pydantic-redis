from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate
from app.utils.logger import CustomLogger
from typing import List, Optional

logger = CustomLogger(__name__)

class CategoryService:
    @staticmethod
    async def create_category(db: Session, category_data: CategoryCreate) -> Category:
        """
        Crea una nueva categoría para un proyecto
        """
        new_category = Category(**category_data.dict())
        db.add(new_category)
        await db.commit()
        await db.refresh(new_category)
        return new_category

    @staticmethod
    async def update_category(db: Session, category_id: str, update_data: CategoryUpdate) -> Category:
        """
        Actualiza una categoría existente
        """
        category = await db.query(Category).filter(Category.id == category_id).first()
        if not category:
            return None
        for key, value in update_data.dict().items():
            setattr(category, key, value)
        await db.commit()
        await db.refresh(category)
        return category

    @staticmethod
    async def delete_category(db: Session, category_id: str) -> bool:
        """
        Elimina una categoría (soft delete)
        """
        category = await db.query(Category).filter(Category.id == category_id).first()
        if not category:
            return False
        category.is_active = False
        await db.commit()
        return True

    @staticmethod
    async def get_category_by_id(db: Session, category_id: str) -> Optional[Category]:
        """
        Obtiene una categoría por su ID
        """
        return await db.query(Category).filter(Category.id == category_id).first()

    @staticmethod
    async def list_categories(db: Session, project_id: str, skip: int = 0, limit: int = 100) -> List[Category]:
        """
        Lista todas las categorías de un proyecto
        """
        return await db.query(Category).filter(Category.project_id == project_id).offset(skip).limit(limit).all()
