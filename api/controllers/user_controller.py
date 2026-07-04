from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from dal.models.user import User
from dal.repositories.user_repository import UserRepository
from api.schemas.user import UserCreate, UserUpdate


class UserController:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def get_all(self, skip: int, limit: int) -> list[User]:
        return self.repo.get_all(skip=skip, limit=limit)

    def get_by_id(self, user_id: int) -> User:
        user = self.repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    def create(self, payload: UserCreate) -> User:
        if self.repo.get_by_email(payload.email):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
        user = User(name=payload.name, email=payload.email)
        return self.repo.create(user)

    def update(self, user_id: int, payload: UserUpdate) -> User:
        user = self.get_by_id(user_id)
        return self.repo.update(user, payload.name, payload.is_active)

    def delete(self, user_id: int) -> None:
        user = self.get_by_id(user_id)
        self.repo.delete(user)
