from typing import Literal
from wsgiref.validate import validator
from pydantic import BaseModel
from schemas.user import User

class TaskBase(BaseModel):
    title: str
    description: str
    status: Literal['bakclog', 'doing', 'done']


    @validator('status')
    def validate_status(cls, value):
        if value not in ['bakclog', 'doing', 'done']:
            raise ValueError('Invalid status')
        return value

class TaskCreate(TaskBase):
    created_by: int
    responsible: int

class Task(TaskBase):
    id: int
    creator: User
    assigned_user: User

    class Config:
        orm_mode = True