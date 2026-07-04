from sqlalchemy.orm import Session
from dal.models.exemple import Exemple
from dal.repositories.base_repository import BaseRepository


class ExempleRepository(BaseRepository[Exemple]):
    def __init__(self, db: Session):
        super().__init__(Exemple, db)

    def get_by_owner(self, owner_id: int) -> list[Exemple]:
        return self.db.query(Exemple).filter(Exemple.owner_id == owner_id).all()

    def update(self, exemple: Exemple, titre: str | None, description: str | None) -> Exemple:
        if titre is not None:
            exemple.titre = titre
        if description is not None:
            exemple.description = description
        self.db.commit()
        self.db.refresh(exemple)
        return exemple
