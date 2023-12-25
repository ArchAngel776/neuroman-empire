from PyQt5.QtGui import QResizeEvent

from lib.gui.element import Element
from lib.gui.element.scrollable.fitter import ScrollableFitter


# Main

class ScrollableHorizontalFitter(ScrollableFitter):
    def fitting(self, content: Element, event: QResizeEvent) -> bool: ...

    def is_scrollbar_visible(self, content: Element) -> bool: ...

    @property
    def scrollbar_size(self) -> int: ...
