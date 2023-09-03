from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from app.utils.logger import CustomLogger
from typing import List, Optional

logger = CustomLogger(__name__)

class TaskService:
    @staticmethod
    async def create_task(db: Session, task_data: TaskCreate) -> Task:
        """
        Crea una nueva tarea
        """
        new_task = Task(**task_data.dict())
        db.add(new_task)
        await db.commit()
        await db.refresh(new_task)
        return new_task

    @staticmethod
    async def update_task(db: Session, task_id: str, update_data: TaskUpdate) -> Task:
        """
        Actualiza una tarea existente
        """
        task = await db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return None
        for key, value in update_data.dict().items():
            setattr(task, key, value)
        await db.commit()
        await db.refresh(task)
        return task

    @staticmethod
    async def delete_task(db: Session, task_id: str) -> bool:
        """
        Elimina una tarea (soft delete)
        """
        task = await db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return False
        task.is_active = False
        await db.commit()
        return True

    @staticmethod
    async def get_task_by_id(db: Session, task_id: str) -> Optional[Task]:
        """
        Obtiene una tarea por su ID
        """
        return await db.query(Task).filter(Task.id == task_id).first()

    @staticmethod
    async def list_tasks(db: Session, project_id: str, skip: int = 0, limit: int = 100) -> List[Task]:
        """
        Lista todas las tareas de un proyecto
        """
        return await db.query(Task).filter(Task.project_id == project_id).offset(skip).limit(limit).all()
