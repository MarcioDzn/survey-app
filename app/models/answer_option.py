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

class AnswerOption(Base):
    __tablename__ = "answer_options"

    answer_id = Column(
        Integer,
        ForeignKey("answers.id"),
        primary_key=True,
    )

    option_id = Column(
        Integer,
        ForeignKey("options.id"),
        primary_key=True,
    )

    answer = relationship("Answer", back_populates="answer_options")
    option = relationship("Option")