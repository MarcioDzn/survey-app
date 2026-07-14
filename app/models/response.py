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

class Response(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    started_at = Column(DateTime(timezone=True))
    submitted_at = Column(DateTime(timezone=True))

    survey = relationship("Survey", back_populates="responses")
    user = relationship("User", back_populates="responses")

    answers = relationship(
        "Answer",
        back_populates="response",
        cascade="all, delete-orphan")
