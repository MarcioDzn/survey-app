from datetime import datetime
from typing import Union

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    name: Union[str]
    email: Union[EmailStr]
    password: Union[str]


class UserRead(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
