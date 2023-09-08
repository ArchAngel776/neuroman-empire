from typing import TypeVar

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QLabel

from lib.gui.element import Element
from lib.gui.window import Window

# Types

TText = TypeVar("TText", bound=Text)


# Main

class Text(QLabel, Element):
    def __init__(self, root: Window, text: str) -> None: ...

    def Color(self: TText, color: QColor) -> TText: ...

    def Align(self: TText, alignment: Qt.Alignment) -> TText: ...

    def Wrap(self: TText) -> TText: ...
