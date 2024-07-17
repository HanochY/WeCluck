from abc import ABC, abstractmethod

class BaseRepository(ABC):
    entity: type
        
    @abstractmethod
    def add(self, **data):
        ...

    @abstractmethod
    def get(self, **filter):
        ...
        
    @abstractmethod
    def edit(self, id: int, **new_data):
        ...

    @abstractmethod
    def remove(self, id: int):
        ...