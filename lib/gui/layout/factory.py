from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

from lib.gui.layout import Layout
from lib.gui.layout.type import LayoutType


# Main

class LayoutFactory:
    def __init__(self, layout_type):
        self._layout_type = layout_type

    @property
    def layout(self):
        match self._layout_type:
            case LayoutType.HORIZONTAL:
                return QHBoxLayout()
            case LayoutType.VERTICAL:
                return QVBoxLayout()
            case _:
                raise ValueError("Unknown layout type")

    def create(self):
        return Layout(self.layout)
