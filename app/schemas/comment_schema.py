from datetime import datetime

from pydantic import BaseModel

from app.schemas.user_schema import UserResponse


class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    id_user: int
    id_task: int


class CommentUpdate(BaseModel):
    content: str


class CommentResponse(CommentBase):
    id: int
    created_at: datetime
    creator: UserResponse
    id_task: int

    class Config:
        orm_mode = True
