from abc import ABC, abstractmethod

class BaseRepository(ABC):

    @staticmethod
    @abstractmethod
    def add(**data):
        ...

    @staticmethod
    @abstractmethod
    def get(**filter):
        ...
        
    @staticmethod
    @abstractmethod
    def edit(id: int, **new_data):
        ...

    @staticmethod
    @abstractmethod
    def remove(id: int):
        ...