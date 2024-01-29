from typing import Self, TypeVar

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QLabel

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element import Element
from lib.gui.window import Window

# Types

TTextSelectableCursor = TypeVar("TTextSelectableCursor", bound=Text)


# Decorators

class SelectableCursor(Decorator[Text, [Text, bool]]):
    def method(self, target: TTextSelectableCursor, selectable: bool = True) -> TTextSelectableCursor: ...


# Main

class Text(QLabel, Element):
    def __init__(self, root: Window, text: str = None) -> None: ...

    @method(SelectableCursor)
    def Selectable(self, selectable: bool = True) -> Self: ...

    def Color(self, color: QColor) -> Self: ...

    def Align(self, alignment: Qt.Alignment) -> Self: ...

    def Wrap(self) -> Self: ...
