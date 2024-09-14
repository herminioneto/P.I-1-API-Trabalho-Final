from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str
    username: str


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserUpdate(BaseModel):
    name: str
    username: str
    current_password: str = Field(..., min_length=8)
    new_password: str = Field(None, min_length=8)


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
