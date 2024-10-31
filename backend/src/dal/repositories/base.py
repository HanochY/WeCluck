from abc import ABC, abstractmethod
from pydantic import BaseModel

class BaseRepository(ABC):
    entity: BaseModel
        
    @abstractmethod
    def add(self, *args, **kwargs):
        ...

    @abstractmethod
    def find(self, *args, **kwargs):
        ...
        
    @abstractmethod
    def edit(self, *args, **kwargs):
        ...

    @abstractmethod
    def remove(self, *args, **kwargs):
        ...