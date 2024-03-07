from typing import TypeVar, Union, Iterable, Callable, Optional, Type, Any

from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QPalette, QColor, QGradient
from PyQt5.QtWidgets import QLayout, QWidget, QApplication

from lib import void

# Types

EntityType = TypeVar("EntityType")
PairType = TypeVar("PairType")

ForEachType = TypeVar("ForEachType")

MapFrom = TypeVar("MapFrom")
MapTo = TypeVar("MapTo")

FilterItem = TypeVar("FilterItem")

MergeType = TypeVar("MergeType")

ItemType = TypeVar("ItemType")

TypeofTarget = TypeVar("TypeofTarget")

FindOneItemType = TypeVar("FindOneItemType")


# Modules

def entities(target: Iterable[EntityType]) -> list[tuple[int, EntityType]]: ...


def pairs(target: Iterable[PairType]) -> list[tuple[PairType, PairType]]: ...


def layout_widget(layout: QLayout) -> QWidget: ...


def palette_color(role: QPalette.ColorRole, color: Union[QColor, Qt.GlobalColor, QGradient]) -> QPalette: ...


def foreach(target: Iterable[ForEachType], callback: Callable[[ForEachType, Optional[int]], void]) -> void: ...


def mapping(target: Iterable[MapFrom], callback: Callable[[MapFrom, Optional[int]], MapTo]) -> list[MapTo]: ...


def filtering(target: Iterable[FilterItem], callback: Callable[[FilterItem, Optional[int]], bool]) -> list[FilterItem]: ...


def merge(**sources: list[MergeType]) -> list[dict[str, MergeType]]: ...


def app() -> QApplication: ...


def bytes_to_string(target: bytes) -> str: ...


def index_of(index: QModelIndex, item_type: Type[ItemType]) -> ItemType: ...


def is_index(index: QModelIndex, *item_type: Type[object]) -> bool: ...


def length(iterable: Iterable[Any]) -> int: ...


def find_one(source: Iterable[FindOneItemType], finder: Callable[[FindOneItemType], bool]) -> bool: ...
