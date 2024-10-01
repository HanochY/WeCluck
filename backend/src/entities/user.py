from pydantic import BaseModel

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    password: str
    
class UserRead(UserBase):
    id: int

class UserUpdate(UserBase):
    name: str | None
    password: str | None
