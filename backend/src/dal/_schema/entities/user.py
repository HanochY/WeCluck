from dal._schema.entities._validator import validate
from pydantic import BaseModel
from typing import TypedDict

class User:
    class Public:
        id: int
        name: str

    class Private:
        id: int
        name: str
        password: str

    class Create:
        name: str
        password: str

    class Update:
        name: str | None
        password: str | None
        
    class Model:

        class Public(BaseModel, super.Public):
            pass

        class Private(BaseModel, super.Private):
            pass

        class Create(BaseModel, super.Create):
            pass

        class Update(BaseModel, super.Update):
            pass
    
    class TypedDict:
        class Create(TypedDict, super.Create):
            pass

        class Update(TypedDict, super.Update):
            pass


    #validate(...)