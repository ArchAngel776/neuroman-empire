from typing import TypeVar, Optional

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QScrollArea

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element import TElement, Element

# Types

TScrollable = TypeVar("TScrollable", bound=Scrollable)
TScrollableXSize = TypeVar("TScrollableXSize", bound=Scrollable)
TScrollableYSize = TypeVar("TScrollableYSize", bound=Scrollable)
TScrollableConfigElement = TypeVar("TScrollableConfigElement", bound=Scrollable)


# Decorators

class ScrollXSize(Decorator[Scrollable, [Scrollable, bool, Optional[int]]]):
    def method(self, target: TScrollableXSize, enabled: bool = True, size: int = None) -> TScrollableXSize: ...


class ScrollYSize(Decorator[Scrollable, [Scrollable, bool, Optional[int]]]):
    def method(self, target: TScrollableYSize, enabled: bool = True, size: int = None) -> TScrollableYSize: ...


class ConfigScrollableElement(Decorator[Scrollable, [Scrollable, Element]]):
    def config(self, target: TScrollableConfigElement, content: TElement) -> ConfigScrollableElement: ...


# Main

class Scrollable(QScrollArea, Element):
    def config(self) -> void: ...

    @method(ScrollXSize)
    def ScrollX(self: TScrollable, enabled: bool = True) -> TScrollable: ...

    @method(ScrollYSize)
    def ScrollY(self: TScrollable, enabled: bool = True) -> TScrollable: ...

    def Align(self: TScrollable, alignment: Qt.Alignment) -> TScrollable: ...

    def Adjust(self: TScrollable, adjust: QScrollArea.SizeAdjustPolicy) -> TScrollable: ...

    @method(ConfigScrollableElement)
    def Content(self: TScrollable, content: Element) -> TScrollable: ...
