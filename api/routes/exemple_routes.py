from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from dal.database import get_db_dependency
from api.controllers.exemple_controller import ExempleController
from api.schemas.exemple import ExempleCreate, ExempleUpdate, ExempleRead

router = APIRouter(prefix="/exemples", tags=["exemples"])


def get_controller(db: Session = Depends(get_db_dependency)) -> ExempleController:
    return ExempleController(db)


@router.get("/", response_model=list[ExempleRead])
def list_exemples(skip: int = 0, limit: int = 100, ctrl: ExempleController = Depends(get_controller)):
    return ctrl.get_all(skip, limit)


@router.get("/{exemple_id}", response_model=ExempleRead)
def get_exemple(exemple_id: int, ctrl: ExempleController = Depends(get_controller)):
    return ctrl.get_by_id(exemple_id)


@router.post("/", response_model=ExempleRead, status_code=status.HTTP_201_CREATED)
def create_exemple(payload: ExempleCreate, ctrl: ExempleController = Depends(get_controller)):
    return ctrl.create(payload)


@router.patch("/{exemple_id}", response_model=ExempleRead)
def update_exemple(exemple_id: int, payload: ExempleUpdate, ctrl: ExempleController = Depends(get_controller)):
    return ctrl.update(exemple_id, payload)


@router.delete("/{exemple_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_exemple(exemple_id: int, ctrl: ExempleController = Depends(get_controller)):
    ctrl.delete(exemple_id)
