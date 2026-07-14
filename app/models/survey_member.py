from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    DateTime, 
    Boolean, 
    ForeignKey, 
    UniqueConstraint,
    func, 
    Enum as SqlEnum)
from sqlalchemy.orm import relationship 
from app.database import Base
from enum import Enum

class MemberRole(str, Enum):
    OWNER = "owner"
    EDITOR = "editor"
    VIEWER = "viewer"


class SurveyMember(Base):
    __tablename__ = "survey_members"

    survey_id = Column(
        Integer, 
        ForeignKey("surveys.id", ondelete="CASCADE"), 
        primary_key=True,
    )
    user_id = Column(
        Integer, 
        ForeignKey("users.id", ondelete="CASCADE"), 
        primary_key=True,
    )
    role = Column(SqlEnum(MemberRole), nullable = False)

    survey = relationship("Survey", back_populates="members")
    user = relationship("User", back_populates="survey_members")

