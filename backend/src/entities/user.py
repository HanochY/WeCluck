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
    id: int

class UserUpdate(UserBase):
    name: str | None
    password: str | None
