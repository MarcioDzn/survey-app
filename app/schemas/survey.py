from datetime import datetime
from typing import Union

from pydantic import BaseModel


class SurveyBase(BaseModel):
    title: str
    description: str
    is_public: bool
    is_active: bool


class SurveyCreate(SurveyBase):
    pass


class SurveyRead(SurveyBase):
    id: int
    code: str
    created_at: datetime


class SurveyUpdate(BaseModel):
    title: Union[str]
    description: Union[str]
    is_public: Union[bool]
    is_active: Union[bool]

    class Config:
        orm_mode = True
