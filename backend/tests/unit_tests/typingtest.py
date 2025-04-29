from pydantic import BaseModel, create_model
from typing import Unpack
from typing_extensions import Annotated, TypedDict
from pydantic import validate_call, ConfigDict

class User(TypedDict):
    id: int
    name: str
    password: str
    
    
def inject_fields(typed_dict: type[TypedDict]) -> BaseModel: 
    def decorator(cls):
        fields = {key: (value, ...) for key, value in typed_dict.__annotations__.items()} 
        new_model = create_model(cls.__name__, **fields) 
        return new_model 
    return decorator

@inject_fields(User)
class UserModel(BaseModel):
    model_config = ConfigDict(strict=True)
    pass

@validate_call
def create_user(**user: UserModel):
    return UserModel(**user)

print(create_user(i="a", name="a", password="b"))
