import bcrypt
from sqlalchemy.orm import Session

from app.models import User as UserModel
from app.schemas.user_schema import UserCreate, UserUpdate


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )


def get_all_users(db: Session):
    return db.query(UserModel).all()


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()


def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = UserModel(
        name=user.name,
        username=user.username,
        password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = get_user(db, user_id)
    if db_user:
        if user.name:
            db_user.name = user.name
        if user.username:
            db_user.username = user.username
        db.commit()
        db.refresh(db_user)

    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return {"detail": "Usuário deletado com sucesso"}
    return {"detail": "Usuário não encontrado"}
