from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QScrollArea

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element import Element


# Decorators

class ScrollXSize(Decorator):
    def method(self, target, enabled=True, size=None):
        if enabled and size:
            target.horizontalScrollBar().setFixedHeight(size)
        return super().method(target, enabled)


class ScrollYSize(Decorator):
    def method(self, target, enabled=True, size=None):
        if enabled and size:
            target.verticalScrollBar().setFixedWidth(size)
        return super().method(target, enabled)


class ConfigScrollableElement(Decorator):
    def config(self, target, content):
        content.config()
        return self


# Main

class Scrollable(QScrollArea, Element):
    def config(self):
        super().config()
        self.setWidgetResizable(True)

    @method(ScrollXSize)
    def ScrollX(self, enabled=True):
        if enabled:
            self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        else:
            self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        return self

    @method(ScrollYSize)
    def ScrollY(self, enabled=True):
        if enabled:
            self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        else:
            self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        return self

    def Align(self, alignment):
        self.setAlignment(alignment)
        return self

    def Adjust(self, adjust):
        self.setSizeAdjustPolicy(adjust)
        return self

    @method(ConfigScrollableElement)
    def Content(self, content):
        self.setWidget(content)
        return self
