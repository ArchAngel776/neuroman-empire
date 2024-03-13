from typing import TypeVar, Self

from PyQt5.QtCore import QModelIndex

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.foundations.data_provider import DataProvider

# Types

TModelIndexProviderSingleIndexValidation = TypeVar("TModelIndexProviderSingleIndexValidation", bound=ModelIndexProvider)


# Decorators

class SingleIndexValidation(Decorator[void, [ModelIndexProvider, *tuple[QModelIndex, ...]]]):
    def config(self, target: TModelIndexProviderSingleIndexValidation, *data: QModelIndex) -> Self: ...


# Main

class ModelIndexProvider(DataProvider[QModelIndex, QModelIndex]):
    _index: QModelIndex

    def __init__(self) -> None: ...

    @method(SingleIndexValidation)
    def add(self, *data: QModelIndex) -> void: ...

    def provide(self) -> QModelIndex: ...

    def clear(self) -> void: ...
