from pydantic import BaseModel
from typing import Type


def validate(private_model: Type[BaseModel], public_model: Type[BaseModel],
             create_model: Type[BaseModel], update_model: Type[BaseModel],
             create_dict: Type[dict], update_dict: Type[dict]):
    pass

#I AM THE DYNAMIC TYPE CHECKING