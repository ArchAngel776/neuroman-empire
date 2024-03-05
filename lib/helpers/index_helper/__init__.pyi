from PyQt5.QtCore import QModelIndex, QAbstractItemModel

from .counter import Counter


# Main

class IndexHelper:
    def index_to_position(self, model: QAbstractItemModel, index: QModelIndex, level: int) -> int: ...

    def position_to_index(self, model: QAbstractItemModel, position: int, level: int) -> QModelIndex: ...

    def recursive_index_to_position(
            self,
            model: QAbstractItemModel,
            index: QModelIndex,
            level: int,
            counter: Counter,
            current_level: int = ...
    ) -> bool: ...

    def recursive_position_to_index(
            self,
            model: QAbstractItemModel,
            position: int,
            level: int,
            counter: Counter,
            current_level: int = ...,
            index: QModelIndex = ...
    ) -> bool: ...
