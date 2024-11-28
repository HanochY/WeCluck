from pydantic import BaseModel
from typing import Type
from abc import ABC

class BaseEntity(ABC):
    _base: Type[BaseModel]
    private: Type[BaseModel]
    public: Type[BaseModel]
    create: Type[BaseModel]
    update: Type[BaseModel]
    db_model: Type[BaseModel]