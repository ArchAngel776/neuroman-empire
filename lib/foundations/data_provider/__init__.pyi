from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from lib import void

# Types

DataType = TypeVar("DataType")


# Main

class DataProvider(ABC, Generic[DataType]):
    @abstractmethod
    def add(self, *data: DataType) -> void: ...

    @abstractmethod
    def provide(self) -> DataType: ...

    @abstractmethod
    def clear(self) -> void: ...
