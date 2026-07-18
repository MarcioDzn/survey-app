from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_survey_service
from app.exceptions import NotFoundError
from app.schemas import SurveyCreate, SurveyRead, SurveyUpdate
from app.services import SurveyService

router = APIRouter(prefix="/survey", tags=["Surveys"])


@router.post("/", response_model=SurveyRead, status_code=status.HTTP_201_CREATED)
def create(
    user_data: SurveyCreate, survey_service: SurveyService = Depends(get_survey_service)
):
    return survey_service.create(user_data)


@router.get("/", response_model=list[SurveyRead], status_code=status.HTTP_200_OK)
def get_all(survey_service: SurveyService = Depends(get_survey_service)):
    return survey_service.get_all()


@router.get("/{id}", response_model=SurveyRead, status_code=status.HTTP_200_OK)
def get_by_id(id: int, survey_service: SurveyService = Depends(get_survey_service)):
    try:
        return survey_service.get_by_id(id)
    except NotFoundError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))
    

@router.get("/code/{code}", response_model=SurveyRead, status_code=status.HTTP_200_OK)
def get_by_code(code: str, survey_service: SurveyService = Depends(get_survey_service)):
    try:
        return survey_service.get_by_code(code)
    except NotFoundError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))


@router.patch("/{id}", response_model=SurveyRead, status_code=status.HTTP_200_OK)
def update(
    id: int,
    user_data: SurveyUpdate,
    survey_service: SurveyService = Depends(get_survey_service),
):
    try:
        return survey_service.update(id, user_data)
    except NotFoundError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))


@router.delete("/{id}", response_model=None, status_code=status.HTTP_200_OK)
def delete(id: int, survey_service: SurveyService = Depends(get_survey_service)):
    try:
        return survey_service.delete(id)
    except NotFoundError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))
