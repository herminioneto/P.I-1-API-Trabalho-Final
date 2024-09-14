from pydantic import BaseModel
from schemas.user import User

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    id_user: int

class Comment(CommentBase):
    id: int
    id_user: int
    user: User

    class Config:
        orm_mode = True