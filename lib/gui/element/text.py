from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QLabel

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.hooks import palette_color
from lib.gui.element import Element


# Decorators

class SelectableCursor(Decorator):
    def method(self, target, selectable=True):
        super().method(target, selectable)
        return target.Cursor(Qt.IBeamCursor) if selectable else target.Cursor(Qt.ArrowCursor)


# Main

class Text(QLabel, Element):
    def __init__(self, root, text=None):
        super().__init__(root)
        self.setText(text)

    @method(SelectableCursor)
    def Selectable(self, selectable=True):
        if selectable:
            self.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        else:
            self.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        return self

    def Color(self, color):
        self.setPalette(palette_color(QPalette.WindowText, color))
        return self

    def Align(self, alignment):
        self.setAlignment(alignment)
        return self

    def Wrap(self):
        self.setWordWrap(True)
        return self
