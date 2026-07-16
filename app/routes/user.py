from fastapi import APIRouter, Depends, status

from app.dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", status_code=status.HTTP_200_OK)
def get_users(user_service=Depends(get_user_service)):
    return user_service.get_all()
