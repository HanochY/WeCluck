from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    password: str

class UserCreate(UserBase):
    pass
class UserRead(UserBase):
    id: int

class UserUpdate(UserBase):
    name: str | None
    password: str | None
