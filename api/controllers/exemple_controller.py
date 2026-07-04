from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from dal.models.exemple import Exemple
from dal.Repositories.exemple_repository import ExempleRepository
from dal.Repositories.user_repository import UserRepository
from api.schemas.exemple import ExempleCreate, ExempleUpdate


class ExempleController:
    def __init__(self, db: Session):
        self.repo = ExempleRepository(db)
        self.user_repo = UserRepository(db)

    def get_all(self, skip: int, limit: int) -> list[Exemple]:
        return self.repo.get_all(skip=skip, limit=limit)

    def get_by_id(self, exemple_id: int) -> Exemple:
        exemple = self.repo.get_by_id(exemple_id)
        if not exemple:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exemple not found")
        return exemple

    def create(self, payload: ExempleCreate) -> Exemple:
        if not self.user_repo.get_by_id(payload.owner_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Owner not found")
        exemple = Exemple(titre=payload.titre, description=payload.description, owner_id=payload.owner_id)
        return self.repo.create(exemple)

    def update(self, exemple_id: int, payload: ExempleUpdate) -> Exemple:
        exemple = self.get_by_id(exemple_id)
        return self.repo.update(exemple, payload.titre, payload.description)

    def delete(self, exemple_id: int) -> None:
        exemple = self.get_by_id(exemple_id)
        self.repo.delete(exemple)
