from typing import Literal, Optional

from pydantic import BaseModel
from schemas.user_schema import UserResponse


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Literal["backlog", "doing", "done"] = "backlog"


class TaskCreate(TaskBase):
    created_by: int
    responsible: int


class TaskResponse(TaskBase):
    id: int
    creator: UserResponse
    assigned_user: UserResponse

    class Config:
        orm_mode = True
