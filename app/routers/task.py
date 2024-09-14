from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import task as crud_task
from schemas.task import TaskCreate, Task
from app.core.database import get_db

router = APIRouter()

@router.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return crud_task.create_task(db=db, task=task)

@router.get("/tasks/", response_model=list[Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_task.get_tasks(db=db, skip=skip, limit=limit)

@router.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud_task.get_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return db_task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud_task.delete_task(db=db, task_id=task_id)
