from abc import ABC, abstractmethod
from pydantic import BaseModel
class BaseRepository(ABC):
    @abstractmethod
    def create(self, *args, **kwargs) -> int:
        ...

    @abstractmethod
    def read(self, *args, **kwargs) -> list[BaseModel | tuple[BaseModel]]:
        ...
        
    @abstractmethod
    def update(self, *args, **kwargs) -> None:
        ...

    @abstractmethod
    def delete(self, *args, **kwargs) -> None:
        ...