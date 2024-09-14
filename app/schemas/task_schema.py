from pydantic import BaseModel
from schemas.user import User

class TaskBase(BaseModel):
    title: str
    description: str
    status: str

class TaskCreate(TaskBase):
    created_by: int
    responsible: int

class Task(TaskBase):
    id: int
    creator: User
    assigned_user: User

    class Config:
        orm_mode = True