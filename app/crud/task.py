from sqlalchemy.orm import Session

from app.models import Task as TaskModel
from app.models import User as UserModel
from app.schemas.task_schema import TaskCreate, TaskUpdate


def get_task(db: Session, task_id: int):
    return db.query(TaskModel).filter(TaskModel.id == task_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TaskModel).all()


def create_task(db: Session, task: TaskCreate):
    created_by_user = (
        db.query(UserModel).filter(UserModel.id == task.created_by).first()
    )
    if not created_by_user:
        return None

    if task.responsible is not None:
        responsible_user = (
            db.query(UserModel).filter(UserModel.id == task.responsible).first()
        )
        if not responsible_user:
            return None

    db_task = TaskModel(
        title=task.title,
        description=task.description,
        status=task.status,
        created_by=task.created_by,
        responsible=task.responsible,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task_id: int, task: TaskUpdate):
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if db_task:
        if task.title:
            db_task.title = task.title
        if task.description:
            db_task.description = task.description
        if task.status:
            db_task.status = task.status
        if task.responsible is not None:
            responsible_user = (
                db.query(UserModel).filter(UserModel.id == task.responsible).first()
            )
            if not responsible_user:
                return None
            db_task.responsible = task.responsible
        db.commit()
        db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int) -> bool:
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return True
    return False
