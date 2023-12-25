from abc import ABC, abstractmethod

from PyQt5.QtGui import QResizeEvent

from lib.gui.element import Element
from lib.gui.element.scrollable import Scrollable


# Main

class ScrollableFitter(ABC):
    _area: Scrollable

    def __init__(self, area: Scrollable) -> None: ...

    @abstractmethod
    def fitting(self, content: Element, event: QResizeEvent) -> bool: ...

    def additional_size(self, content: Element) -> int: ...

    @abstractmethod
    def is_scrollbar_visible(self, content: Element) -> bool: ...

    @property
    def area(self) -> Scrollable: ...

    @property
    @abstractmethod
    def scrollbar_size(self) -> int: ...
