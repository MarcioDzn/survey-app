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


class QuestionType(str, Enum):
    TEXT = "text"
    LONG_TEXT = "long_text"
    NUMBER = "number"
    BOOLEAN = "boolean"
    SINGLE_CHOICE = "single_choice"
    MULTIPLE_CHOICE = "multiple_choice"
    RATING = "rating"


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"), nullable=False)

    title = Column(String(255), nullable=False)
    description = Column(String(1000))
    type = Column(SqlEnum(QuestionType), nullable=False)
    required = Column(Boolean, default=True)
    position = Column(Integer, nullable=False)

    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


    survey = relationship("Survey", back_populates="questions")

    # apenas uma posição por survey
    __table_args__ = (
        UniqueConstraint(
            "survey_id", 
            "position", 
            name="uq_question_survey_position"
        ),
    )