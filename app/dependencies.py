from fastapi import Depends

from app.database import SessionLocal
from app.services import UserService, SurveyService
from app.repositories import UserRepository, SurveyRepository


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def get_user_service(session = Depends(get_session)):
    user_repository = UserRepository(session)
    return UserService(user_repository, session)


def get_survey_service(session = Depends(get_session)):
    survey_repository = SurveyRepository(session)
    return SurveyService(survey_repository, session)