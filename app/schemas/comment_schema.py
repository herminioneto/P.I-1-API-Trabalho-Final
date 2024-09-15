from pydantic import BaseModel

from app.schemas.user_schema import UserResponse


class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    id_user: int


class CommentUpdate(BaseModel):
    content: str


class CommentResponse(CommentBase):
    id: int
    creator: UserResponse

    class Config:
        orm_mode = True
