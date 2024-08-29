from abc import ABC, abstractmethod

class BaseRepository(ABC):
    entity: type
        
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