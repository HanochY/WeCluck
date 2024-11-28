from abc import ABC, abstractmethod
from dal._schema.entities._base import BaseEntity
from utils.basemodel_to_typeddict import basemodel_to_typeddict
from typing import Unpack, Type
from pydantic import BaseModel

class BaseRepository(ABC):
    entity: Type[BaseEntity]    
    add_kwargs: dict
    edit_kwargs: dict
    
    @abstractmethod
    def __init__(self, entity: Type[BaseEntity]):
        self.entity = entity
        self.add_kwargs = basemodel_to_typeddict(entity.create)
        self.edit_kwargs = basemodel_to_typeddict(entity.update)
    
    @abstractmethod
    def add(self, **add_kwargs) -> int:
        ...

    @abstractmethod
    def find(self, *args, **kwargs) -> list[BaseModel | tuple[BaseModel]]:
        ...
        
    @abstractmethod
    def edit(self, *args, **edit_kwargs) -> None:
        ...

    @abstractmethod
    def remove(self, id: int, *args) -> None:
        ...