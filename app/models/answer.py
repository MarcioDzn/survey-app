from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    DateTime, 
    Boolean, 
    ForeignKey, 
    UniqueConstraint, 
    func)
from sqlalchemy.orm import relationship 
from app.database import Base

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    response_id = Column(Integer, ForeignKey("responses.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    value = Column(String)

    response = relationship("Response", back_populates="answers")
    question = relationship("Question", back_populates="answers")

    answer_options = relationship(
        "AnswerOption", 
        back_populates="answer", 
        cascade="all, delete-orphan")

    __table_args__ = (
        UniqueConstraint(
            "response_id",
            "question_id",
            name="uq_answer_response_question"
        ),
    )