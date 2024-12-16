
from uuid import UUID
from utils.exceptions import *
from dal.sql.forum.tables._common import SQLModelCommon
from dal._schema.resources._generic import GenericOutput, GenericCreate, GenericUpdate
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T', bound=SQLModelCommon) # Any conventional SQLAlchemy ORM object
C = TypeVar('C', bound=GenericCreate)  # Any Create object
U = TypeVar('U', bound=GenericUpdate)  # Any Update object
O = TypeVar('O', bound=GenericOutput)  # Any Output object
class Controller(ABC, Generic[T, C, U, O]):
    db_model: type[T]
    
    @abstractmethod
    async def create(self, data: C) -> UUID | None:        
        pass
    @abstractmethod
    async def read_by_id(self, id: UUID) -> O | None:
        pass
    @abstractmethod
    async def read_all(self) -> list[O] | None:
        pass
    @abstractmethod
    async def update(self, id: UUID, new_data: U) -> None:
        pass
    @abstractmethod
    async def delete(self, id: UUID) -> None:
        pass
    @abstractmethod
    async def undelete(self, id: UUID) -> None:
        pass
    @abstractmethod
    async def hard_delete(self, id: UUID) -> None:
        pass
    