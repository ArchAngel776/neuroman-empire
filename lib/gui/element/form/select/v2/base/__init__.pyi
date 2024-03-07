from typing import Optional, Any, Iterable, Union, TypeVar, ClassVar

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QComboBox, QWidget

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.foundations.data_provider.model_index_provider import ModelIndexProvider
from lib.foundations.data_provider.string_list_provider import StringListProvider
from lib.helpers.index_helper import IndexHelper

# Types

TQComboBox2PreventRoot = TypeVar("TQComboBox2PreventRoot", bound=QComboBox2)

TQComboBox2EditableIndexChanged = TypeVar("TQComboBox2EditableIndexChanged", bound=QComboBox2)

TQComboBox2ClearRootProvider = TypeVar("TQComboBox2ClearRootProvider", bound=QComboBox2)


# Decorators

class PreventRoot(Decorator[void, [QComboBox2, int]]):
    def method(self, target: TQComboBox2PreventRoot, index: int) -> void: ...


class EditableIndexChanged(Decorator[void, QComboBox2, Optional[str]]):
    def method(self, target: TQComboBox2EditableIndexChanged, text: Optional[str]) -> void: ...


class ClearRootProvider(Decorator[void, [QComboBox2, int]]):
    def method(self, target: TQComboBox2ClearRootProvider, index: int) -> void: ...


# Main

class QComboBox2(QComboBox):
    HIERARCHY_LEVEL: ClassVar[int] = ...

    HITS: ClassVar[int] = ...

    class Position(int):
        NONE = ... #type: QComboBox2.Position
        START = ... #type: QComboBox2.Position

    _index_helper: IndexHelper

    _group_id_provider: StringListProvider

    _root_index_provider: ModelIndexProvider

    def __init__(self, parent: Optional[QWidget] = ...) -> None: ...

    def addItem(self, text: Optional[str], userData: Any = ...) -> void: ...

    def addItems(self, texts: Iterable[Optional[str]]) -> void: ...

    def currentIndex(self) -> int: ...

    def findData(
            self,
            data: Any,
            role: Qt.ItemDataRole = ...,
            flags: Union[Qt.MatchFlags, Qt.MatchFlag] = ...
    ) -> int: ...

    def findText(self, text: Optional[str], flags: Union[Qt.MatchFlags, Qt.MatchFlag] = ...) -> int: ...

    def insertItem(self, index: int, text: Optional[str], userData: Any = ...) -> void: ...

    def insertItems(self, index: int, texts: Iterable[Optional[str]]) -> void: ...

    def itemData(self, index: int, role: Qt.ItemDataRole = ...) -> Any: ...

    def itemIcon(self, index: int) -> QIcon: ...

    def itemText(self, index: int) -> str: ...

    def setItemData(self, index: int, value: Any, role: Qt.ItemDataRole = ...) -> void: ...

    def setItemIcon(self, index: int, icon: QIcon) -> void: ...

    def setItemText(self, index: int, text: Optional[str]) -> void: ...

    def addGroup(self, group_id: str, name: Optional[str] = ...) -> void: ...

    def addGroups(self, group_ids: Iterable[str]) -> void: ...

    def addOption(self, group_id: str, title: str, data: Any = ...) -> void: ...

    def addOptions(self, group_id: str, titles: str) -> void: ...

    def findGroupId(self, group_id: str) -> int: ...

    def findGroupName(self, name: Optional[str], flags: Union[Qt.MatchFlags, Qt.MatchFlag] = ...) -> int: ...

    def findOptionTitle(
            self,
            group_id: str,
            title: Optional[str],
            flags: Union[Qt.MatchFlags, Qt.MatchFlag] = ...
    ) -> int: ...

    def findOptionData(self, group_id: str, data: Any, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = ...) -> int: ...

    def groupId(self, index: int) -> str: ...

    def groupName(self, index: int) -> str: ...

    def insertGroup(self, index: int, group_id: str, name: Optional[str] = ...) -> void: ...

    def insertGroups(self, index: int, group_ids: Iterable[str]) -> void: ...

    def insertOption(self, group_id: str, index: int, title: str, data: Any = ...) -> void: ...

    def insertOptions(self, group_id: str, index: int, titles: Iterable[str]) -> void: ...

    def optionData(self, group_id: str, index: int) -> Any: ...

    def optionTitle(self, group_id: str, index: int) -> str: ...

    @method(PreventRoot)
    def setCurrentIndex(self, index: int) -> void: ...

    @method(EditableIndexChanged)
    def setCurrentText(self, text: Optional[str]) -> void: ...

    def setGroupName(self, index: int, name: Optional[str]) -> void: ...

    def setOptionData(self, group_id: str, index: int, userData: Any = ...) -> void: ...

    def setOptionTitle(self, group_id: str, index: int, title: Optional[str]) -> void: ...

    # Slots

    @method(ClearRootProvider)
    def storeRoot(self) -> void: ...

    @property
    def index_helper(self) -> IndexHelper: ...

    @property
    def group_id_provider(self) -> StringListProvider: ...

    @property
    def root_index_provider(self) -> ModelIndexProvider: ...
