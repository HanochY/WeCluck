from abc import ABC, abstractmethod
from backend.src.dal._schema.entities.base import BaseEntity
from src.utils.basemodel_to_typeddict import basemodel_to_typeddict
from typing import Unpack

class BaseRepository(ABC):
    entity: BaseEntity
    
    @abstractmethod
    def add(self, **kwargs: Unpack[typeddict...]):
        ...

    @abstractmethod
    def find(self, *args, **kwargs) -> list[BaseEntity.Public | tuple[BaseEntity.Public]]:
        ...
        
    @abstractmethod
    def edit(self, *args, **kwargs):
        ...

    @abstractmethod
    def remove(self, *args, **kwargs):
        ...