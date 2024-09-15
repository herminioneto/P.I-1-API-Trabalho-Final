from typing import Literal, Optional

from pydantic import BaseModel

from app.schemas.user_schema import UserResponse


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Literal["backlog", "doing", "done"] = "backlog"


class TaskCreate(TaskBase):
    created_by: int
    responsible: Optional[int] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[Literal["backlog", "doing", "done"]] = None
    responsible: Optional[int] = None


class TaskResponse(TaskBase):
    id: int
    creator: UserResponse
    assigned_user: Optional[UserResponse]

    class Config:
        orm_mode = True
