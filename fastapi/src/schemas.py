from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class TodoCreate(BaseModel):
    title: str
    description: str


class TodoGet(TodoCreate):
    id: int

    class Config:
        orm_mode = True


class UserRead(BaseModel):
    id: int
    username: str
    is_active: bool

    class Config:
        orm_mode = True
