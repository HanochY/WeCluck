from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    
class UserPublic(UserBase):
    id: int
    
class UserPrivate(UserPublic):
    password: str

class UserCreate(UserBase):
    password: str
    
class UserRead(UserBase):
    id: int | None
    name: str | None
    password: str | None

class UserUpdate(UserBase):
    name: str | None
    password: str | None
