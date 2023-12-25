from PyQt5.QtGui import QResizeEvent

from lib.gui.element import Element
from lib.gui.element.scrollable.fitter import ScrollableFitter


# Main

class ScrollableVerticalFitter(ScrollableFitter):
    def fitting(self, content: Element, event: QResizeEvent):
        self.area.setFixedHeight(event.size().height() + self.additional_size(content))
        return True

    def is_scrollbar_visible(self, content: Element):
        return content.width() > self.area.width()

    @property
    def scrollbar_size(self):
        return self.area.horizontalScrollBar().height()
