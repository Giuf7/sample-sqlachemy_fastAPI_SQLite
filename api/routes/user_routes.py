from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from dal.database import get_db
from api.controllers.user_controller import UserController
from api.schemas.user import UserCreate, UserUpdate, UserRead, UserReadWithItems

router = APIRouter(prefix="/users", tags=["users"])


def get_controller(db: Session = Depends(get_db)) -> UserController:
    return UserController(db)


@router.get("/", response_model=list[UserRead])
def list_users(skip: int = 0, limit: int = 100, ctrl: UserController = Depends(get_controller)):
    return ctrl.get_all(skip, limit)


@router.get("/{user_id}", response_model=UserReadWithItems)
def get_user(user_id: int, ctrl: UserController = Depends(get_controller)):
    return ctrl.get_by_id(user_id)


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, ctrl: UserController = Depends(get_controller)):
    return ctrl.create(payload)


@router.patch("/{user_id}", response_model=UserRead)
def update_user(user_id: int, payload: UserUpdate, ctrl: UserController = Depends(get_controller)):
    return ctrl.update(user_id, payload)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, ctrl: UserController = Depends(get_controller)):
    ctrl.delete(user_id)
