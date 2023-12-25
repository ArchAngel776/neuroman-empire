from typing import TypeVar, Generic, Any

from PyQt5.QtCore import QAbstractItemModel, QModelIndex, Qt

from lib.gui.element.form.select import SelectBox
from .group import SelectModelGroup

# Types

SelectModelData = TypeVar("SelectModelData")


# Main

class SelectModel(QAbstractItemModel, Generic[SelectModelData]):
    _groups: list[SelectModelGroup[SelectModelData]]

    def __init__(self, parent: SelectBox[SelectModelData]) -> None: ...

    def index(self, row: int, column: int, parent: QModelIndex = ...) -> QModelIndex: ...

    def parent(self, child: QModelIndex = ...) -> Any: ...

    def flags(self, index: QModelIndex) -> Qt.ItemFlags: ...

    def data(self, index: QModelIndex, role: Qt.ItemDataRole = ...) -> str: ...

    def rowCount(self, parent: QModelIndex = ...) -> int: ...

    def columnCount(self, parent: QModelIndex = ...) -> int: ...

    def setData(self, index: QModelIndex, value: str, role: Qt.ItemDataRole = ...) -> bool: ...

    def insertRows(self, row: int, count: int, parent: QModelIndex = ...) -> bool: ...

    def removeRows(self, row: int, count: int, parent: QModelIndex = ...) -> bool: ...

    @property
    def groups(self) -> list[SelectModelGroup[SelectModelData]]: ...
