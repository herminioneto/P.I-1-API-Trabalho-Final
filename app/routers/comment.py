from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.crud import comment as crud_comment
from app.schemas.comment_schema import CommentCreate, CommentResponse, CommentUpdate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/comments/", response_model=list[CommentResponse])
def read_comments(db: Session = Depends(get_db)):
    return crud_comment.get_comments(db=db)


@router.get("/comments/{comment_id}", response_model=CommentResponse)
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = crud_comment.get_comment(db=db, comment_id=comment_id)
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comentário não encontrado")
    return db_comment


@router.post("/comments/", response_model=CommentResponse)
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    return crud_comment.create_comment(db=db, comment=comment)


@router.put("/comments/{comment_id}", response_model=CommentResponse)
def update_comment(
    comment_id: int, comment: CommentUpdate, db: Session = Depends(get_db)
):
    db_comment = crud_comment.update_comment(
        db=db, comment_id=comment_id, comment=comment
    )
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comentário não encontrado")
    return db_comment


@router.delete("/comments/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    result = crud_comment.delete_comment(db=db, comment_id=comment_id)
    if result["detail"] == "Comentário não encontrado":
        raise HTTPException(status_code=404, detail="Comentário não encotrado")
    return result
