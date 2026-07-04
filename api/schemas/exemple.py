from pydantic import BaseModel


class ExempleBase(BaseModel):
    titre: str
    description: str | None = None


class ExempleCreate(ExempleBase):
    owner_id: int


class ExempleUpdate(BaseModel):
    titre: str | None = None
    description: str | None = None


class ExempleRead(ExempleBase):
    id: int
    owner_id: int

    model_config = {"from_attributes": True}
