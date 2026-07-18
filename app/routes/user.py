from fastapi import APIRouter, Depends, status, HTTPException

from app.services import UserService
from app.dependencies import get_user_service
from app.schemas import UserRead, UserCreate

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create(user_data: UserCreate, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.create(user_data)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="E-mail já cadastrado")


@router.get("/", response_model=list[UserRead], status_code=status.HTTP_200_OK)
def get_users(user_service: UserService=Depends(get_user_service)):
    return user_service.get_all()
