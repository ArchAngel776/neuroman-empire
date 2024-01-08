from typing import TypeVar, Union, Iterable, Callable, Optional

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPalette, QColor, QGradient
from PyQt5.QtWidgets import QLayout, QWidget, QApplication

from lib import void

# Types

EntityType = TypeVar("EntityType")
PairType = TypeVar("PairType")

ForEachType = TypeVar("ForEachType")

MapFrom = TypeVar("MapFrom")
MapTo = TypeVar("MapTo")

MergeType = TypeVar("MergeType")


# Modules

def entities(target: Iterable[EntityType]) -> list[tuple[int, EntityType]]: ...


def pairs(target: Iterable[PairType]) -> list[tuple[PairType, PairType]]: ...


def layout_widget(layout: QLayout) -> QWidget: ...


def palette_color(role: QPalette.ColorRole, color: Union[QColor, Qt.GlobalColor, QGradient]) -> QPalette: ...


def foreach(target: Iterable[ForEachType], callback: Callable[[ForEachType, Optional[int]], void]) -> void: ...


def mapping(target: Iterable[MapFrom], callback: Callable[[MapFrom, Optional[int]], MapTo]) -> list[MapTo]: ...


def merge(**sources: list[MergeType]) -> list[dict[str, MergeType]]: ...


def app() -> QApplication: ...


def bytes_to_string(target: bytes) -> str: ...
