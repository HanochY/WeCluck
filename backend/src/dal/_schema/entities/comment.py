from dal._schema.entities._validator import validate
from pydantic import BaseModel
from typing import TypedDict

class Comment:
    class Public:
        id: int
        uid: int
        title: str
        content: str
        topic_id: int

    class Private:
        id: int
        uid: int
        title: str
        content: str
        topic_id: int

    class Create:
        uid: int
        title: str
        content: str
        topic_id: int

    class Update:
        uid: int | None
        title: str | None
        content: str | None
        topic_id: int | None

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