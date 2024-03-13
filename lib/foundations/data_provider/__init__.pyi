from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from lib import void

# Types

DataType = TypeVar("DataType")
ReturnType = TypeVar("ReturnType")


# Main

class DataProvider(ABC, Generic[DataType, ReturnType]):
    @abstractmethod
    def add(self, *data: DataType) -> void: ...

    @abstractmethod
    def provide(self) -> ReturnType: ...

    @abstractmethod
    def clear(self) -> void: ...
