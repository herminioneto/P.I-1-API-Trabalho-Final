from pydantic import BaseModel
from schemas.user_schema import UserResponse


class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    id_user: int


class CommentUpdate(BaseModel):
    content: str


class CommentResponse(CommentBase):
    id: int
    id_user: int
    user: UserResponse

    class Config:
        orm_mode = True
