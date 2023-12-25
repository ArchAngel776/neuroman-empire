from abc import ABC, abstractmethod
from typing import Self, TypeVar, Optional

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QScrollArea

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.event.scroll_area_content import ScrollAreaContent
from lib.gui.element import Element
from .fitter import ScrollableFitter

# Types

TScrollableFit = TypeVar("TScrollableFit", bound=Scrollable)
TScrollableXSize = TypeVar("TScrollableXSize", bound=Scrollable)
TScrollableYSize = TypeVar("TScrollableYSize", bound=Scrollable)
TScrollableConfigScrollableElement = TypeVar("TScrollableConfigScrollableElement", bound=Scrollable)
TScrollableEmitScrollContentEvent = TypeVar("TScrollableEmitScrollContentEvent", bound=Scrollable)


# Base

class ScrollFit(Decorator[Scrollable, [Scrollable, bool]], ABC):
    def method(self, target: TScrollableFit, enabled: bool = True) -> TScrollableFit: ...

    def scroll_content_fitting(self, area: Scrollable, event: ScrollAreaContent): ...

    @abstractmethod
    def createFitter(self, area: Scrollable) -> ScrollableFitter: ...


# Decorators

class ScrollXSize(Decorator[Scrollable, [Scrollable, bool, Optional[int]]]):
    def method(self, target: TScrollableXSize, enabled: bool = True, size: int = None) -> TScrollableXSize: ...


class ScrollXFit(ScrollFit):
    def createFitter(self, area: Scrollable) -> ScrollableFitter: ...


class ScrollYSize(Decorator[Scrollable, [Scrollable, bool, Optional[int]]]):
    def method(self, target: TScrollableYSize, enabled: bool = True, size: int = None) -> TScrollableYSize: ...


class ScrollYFit(ScrollFit):
    def createFitter(self, area: Scrollable) -> ScrollableFitter: ...


class ConfigScrollableElement(Decorator[Scrollable, [Scrollable, Element]]):
    def config(self, target: TScrollableConfigScrollableElement, content: Element) -> Self: ...


class EmitScrollContentEvent(Decorator[Scrollable, [Scrollable, Element]]):
    def method(self, target: TScrollableEmitScrollContentEvent, content: Element) -> TScrollableEmitScrollContentEvent: ...


# Main

class Scrollable(QScrollArea, Element):
    def config(self) -> void: ...

    @method(ScrollXFit)
    @method(ScrollXSize)
    def ScrollX(self, enabled: bool = True) -> Self: ...

    @method(ScrollYFit)
    @method(ScrollYSize)
    def ScrollY(self, enabled: bool = True) -> Self: ...

    def Align(self, alignment: Qt.Alignment) -> Self: ...

    def Adjust(self, adjust: QScrollArea.SizeAdjustPolicy) -> Self: ...

    @method(ConfigScrollableElement)
    @method(EmitScrollContentEvent)
    def Content(self, content: Element) -> Self: ...
