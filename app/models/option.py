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

class Option(Base):
    __tablename__ = "options"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False) 
    label = Column(String(255), nullable=False)
    position = Column(Integer, nullable=False)

    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    question = relationship("Question", back_populates="options")

    # apenas uma posição por opção
    __table_args__ = (
        UniqueConstraint(
            "question_id", 
            "position", 
            name="uq_option_question_position"
        ),
    )