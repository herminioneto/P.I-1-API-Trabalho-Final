from sqlalchemy.orm import Session

from app.models import Comment as CommentModel
from app.schemas.comment_schema import CommentCreate, CommentUpdate


def get_comments(db: Session):
    return db.query(CommentModel).all()


def get_comment(db: Session, comment_id: int):
    return db.query(CommentModel).filter(CommentModel.id == comment_id).first()


def create_comment(db: Session, comment: CommentCreate):
    db_comment = CommentModel(
        content=comment.content,
        id_user=comment.id_user,
        id_task=comment.id_task,
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def update_comment(db: Session, comment_id: int, comment: CommentUpdate):
    db_comment = db.query(CommentModel).filter(CommentModel.id == comment_id).first()
    if db_comment:
        db_comment.content = comment.content
        db.commit()
        db.refresh(db_comment)
    return db_comment


def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(CommentModel).filter(CommentModel.id == comment_id).first()
    if db_comment:
        db.delete(db_comment)
        db.commit()
        return {"detail": "Comentário deletado com sucesso"}
    return {"detail": "Comentário não encontrado"}
