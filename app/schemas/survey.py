from datetime import datetime
from typing import Optional

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
    title: Optional[str] = None
    description: Optional[str] = None
    is_public: Optional[bool] = None
    is_active: Optional[bool] = None

    class Config:
        orm_mode = True
