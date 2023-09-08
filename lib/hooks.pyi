from typing import TypeVar, Union, Iterable

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QGradient
from PyQt5.QtWidgets import QLayout, QWidget

# Types

EntityType = TypeVar("EntityType")
PairType = TypeVar("PairType")


# Modules

def entities(target: Iterable[EntityType]) -> list[tuple[int, EntityType]]: ...


def pairs(target: Iterable[PairType]) -> list[tuple[PairType, PairType]]: ...


def layout_widget(layout: QLayout) -> QWidget: ...


def palette_color(role: QPalette.ColorRole, color: Union[QColor, Qt.GlobalColor, QGradient]) -> QPalette: ...
