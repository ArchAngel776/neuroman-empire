from typing import Self

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QLabel

from lib.gui.element import Element
from lib.gui.window import Window


# Main

class Text(QLabel, Element):
    def __init__(self, root: Window, text: str) -> None: ...

    def Color(self, color: QColor) -> Self: ...

    def Align(self, alignment: Qt.Alignment) -> Self: ...

    def Wrap(self) -> Self: ...
