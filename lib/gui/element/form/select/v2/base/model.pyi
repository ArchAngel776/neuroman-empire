from typing import Optional, Union, Generic, TypeVar, overload, Type

from PyQt5.QtCore import QAbstractItemModel, QModelIndex, Qt

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.foundations.data_provider.string_list_provider import StringListProvider
from lib.gui.element.form.select.v2 import Select2Box
from lib.gui.element.form.select.v2.data import Select2Container
from lib.gui.element.form.select.v2.data.group import Select2Group
from lib.gui.element.form.select.v2.data.option import Select2Option

# Types

Select2ModelData = TypeVar("Select2ModelData")

TSelect2ModelUpdateData = TypeVar("TSelect2ModelUpdateData", bound=Select2Model)
Select2ModelUpdateData = TypeVar("Select2ModelUpdateData")

TSelect2ModelInsertCycle = TypeVar("TSelect2ModelInsertCycle", bound=Select2Model)
Select2ModelInsertCycleData = TypeVar("Select2ModelInsertCycleData")

TSelect2ModelRemoveCycle = TypeVar("TSelect2ModelRemoveCycle", bound=Select2Model)
Select2ModelRemoveCycleData = TypeVar("Select2ModelRemoveCycleData")


# Decorators

class UpdateData(
    Decorator[bool, [Select2Model[Select2ModelUpdateData], QModelIndex, str, Qt.ItemDataRole]],
    Generic[Select2ModelUpdateData]
):
    def method(
            self,
            target: TSelect2ModelUpdateData,
            index: QModelIndex,
            value: str,
            role: Qt.ItemDataRole = ...
    ) -> bool: ...


class InsertCycle(
    Decorator[bool, [Select2Model[Select2ModelInsertCycleData], int, int, QModelIndex]],
    Generic[Select2ModelInsertCycleData]
):
    def method(self, target: TSelect2ModelInsertCycle, row: int, count: int, parent: QModelIndex = ...) -> bool: ...


class RemoveCycle(
    Decorator[bool, [Select2Model[Select2ModelRemoveCycleData], int, int, QModelIndex]],
    Generic[Select2ModelRemoveCycleData]
):
    def method(self, target: TSelect2ModelRemoveCycle, row: int, count: int, parent: QModelIndex = ...) -> bool: ...


# Main

class Select2Model(QAbstractItemModel, Generic[Select2ModelData]):
    _container: Select2Container[Select2ModelData]

    _group_id_provider: StringListProvider

    def __init__(self, parent: Select2Box[Select2ModelData], group_id_provider: StringListProvider) -> None: ...

    @staticmethod
    @overload
    def item_type(index: QModelIndex) -> Type[Select2Group[Select2ModelData]]: ...

    @staticmethod
    @overload
    def item_type(index: QModelIndex) -> Type[Select2Option[Select2ModelData]]: ...

    @staticmethod
    @overload
    def item_type(index: QModelIndex) -> None: ...

    @staticmethod
    def item_type(
            index: QModelIndex
    ) -> Optional[Type[Select2Group[Select2ModelData]] | Type[Select2Option[Select2ModelData]]]: ...

    def index(self, row: int, column: int, parent: QModelIndex = ...) -> QModelIndex: ...

    def parent(self, child: QModelIndex = ...) -> QModelIndex: ...

    def flags(self, index: QModelIndex) -> Qt.ItemFlags: ...

    @overload
    def data(self, index: QModelIndex, role: Qt.ItemDataRole.DisplayRole = ...) -> str: ...

    @overload
    def data(self, index: QModelIndex, role: Qt.ItemDataRole.UserRole = ...) -> Optional[Select2ModelData]: ...

    def data(self, index: QModelIndex, role: Qt.ItemDataRole = ...) -> Optional[Union[str, Select2ModelData]]: ...

    def rowCount(self, parent: QModelIndex = ...) -> int: ...

    def columnCount(self, parent: QModelIndex = ...) -> int: ...

    @overload
    def setData(
            self,
            index: QModelIndex,
            value: str,
            role: Qt.ItemDataRole.DisplayRole = ...
    ) -> bool: ...

    @overload
    def setData(
            self,
            index: QModelIndex,
            value: Optional[Select2ModelData],
            role: Qt.ItemDataRole.UserRole = ...
    ) -> bool: ...

    @method(UpdateData[Select2ModelData])
    def setData(
            self,
            index: QModelIndex,
            value: Optional[Union[str, Select2ModelData]],
            role: Qt.ItemDataRole = ...
    ) -> bool: ...

    @method(InsertCycle[Select2ModelData])
    def insertRows(self, row: int, count: int, parent: QModelIndex = ...) -> bool: ...

    @method(RemoveCycle[Select2ModelData])
    def removeRows(self, row: int, count: int, parent: QModelIndex = ...) -> bool: ...

    @property
    def container(self) -> Select2Container[Select2ModelData]: ...

    @property
    def group_id_provider(self) -> StringListProvider: ...
