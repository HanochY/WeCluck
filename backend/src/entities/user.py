from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    class Config:
        orm_mode = True
    
class UserPublic(UserBase):
    id: int
    
class UserPrivate(UserPublic):
    password: str

class UserCreate(UserBase):
    password: str
    
class UserRead(BaseModel):
    id: int | None
    name: str | None
    password: str | None

class UserUpdate(BaseModel):
    name: str | None
    password: str | None
