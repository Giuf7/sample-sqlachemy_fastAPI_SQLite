from sqlalchemy.orm import Session
from dal.models.user import User
from dal.Repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session):
        super().__init__(User, db)

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def update(self, user: User, name: str | None, is_active: bool | None) -> User:
        if name is not None:
            user.name = name
        if is_active is not None:
            user.is_active = is_active
        self.db.commit()
        self.db.refresh(user)
        return user
