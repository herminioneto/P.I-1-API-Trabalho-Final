from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.crud import user as crud_user
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/users", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = crud_user.get_all_users(db)
    return users


@router.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud_user.get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user


@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db=db, user=user)


@router.patch("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return crud_user.update_user(db=db, user_id=user_id, user=user)


@router.delete("/users/{user_id}")
def delete_comment(user_id: int, db: Session = Depends(get_db)):
    result = crud_user.delete_user(db=db, user_id=user_id)
    if result["detail"] == "Usuário não encontrado":
        raise HTTPException(status_code=404, detail="Usuário não encotrado")
    return result
