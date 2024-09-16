from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str
    username: str


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserUpdate(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
