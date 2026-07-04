from pydantic import BaseModel, EmailStr
from api.schemas.exemple import ExempleRead


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: str | None = None
    is_active: bool | None = None


class UserRead(UserBase):
    id: int
    is_active: bool

    model_config = {"from_attributes": True}


class UserReadWithExemples(UserRead):
    exemples: list[ExempleRead] = []
