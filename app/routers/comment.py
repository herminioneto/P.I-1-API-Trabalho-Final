from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import comment as crud_comment
from schemas.comment import CommentCreate, Comment
from app.core.database import get_db

router = APIRouter()

@router.post("/comments/", response_model=Comment)
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    return crud_comment.create_comment(db=db, comment=comment)

@router.get("/comments/", response_model=list[Comment])
def read_comments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_comment.get_comments(db=db, skip=skip, limit=limit)
