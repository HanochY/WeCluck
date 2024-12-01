from dal._schema.entities._validator import validate
from pydantic import BaseModel
from typing import TypedDict

class Topic:
    class Public:
        uid: int
        name: str
        id: int

    class Private:
        uid: int
        name: str
        id: int

    class Create:
        uid: int
        name: str

    class Update:
        uid: int | None
        name: str | None
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