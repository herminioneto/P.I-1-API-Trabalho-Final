from sqlalchemy.orm import Session
from models.comment import Comment as CommentModel
from schemas.comment import CommentCreate

def create_comment(db: Session, comment: CommentCreate):
    db_comment = CommentModel(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(CommentModel).offset(skip).limit(limit).all()
