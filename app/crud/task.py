from sqlalchemy.orm import Session
from models.task import Task as TaskModel
from schemas.task import TaskCreate

def create_task(db: Session, task: TaskCreate):
    db_task = TaskModel(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int):
    return db.query(TaskModel).filter(TaskModel.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TaskModel).offset(skip).limit(limit).all()

def delete_task(db: Session, task_id: int):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return {"detail": "Tarefa deletada com sucesso"}
    return {"detail": "Tarefa não encontrada"}
