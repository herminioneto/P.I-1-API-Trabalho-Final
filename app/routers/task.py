from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.crud import task as crud_task
from app.schemas.task_schema import TaskCreate, TaskResponse, TaskUpdate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud_task.get_task(db=db, task_id=task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return db_task


@router.get("/tasks/", response_model=List[TaskResponse])
def read_filtered_or_all_tasks(
    created_by: Optional[int] = None,
    responsible: Optional[int] = None,
    status: Optional[str] = None,
    db: Session = Depends(get_db),
):
    tasks = crud_task.get_filtered_tasks(
        db=db, created_by=created_by, responsible=responsible, status=status
    )
    return tasks


@router.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    created_task = crud_task.create_task(db=db, task=task)
    if not created_task:
        raise HTTPException(
            status_code=404, detail="Usuário(s) referenciado(s) não encontrado(s)"
        )
    return created_task


@router.patch("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    updated_task = crud_task.update_task(db=db, task_id=task_id, task=task)
    if not updated_task:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada ou usuário responsável inválido",
        )
    return updated_task


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    success = crud_task.delete_task(db=db, task_id=task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"detail": "Tarefa deletada com sucesso"}
