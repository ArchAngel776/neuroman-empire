from typing import Self

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

from lib import void
from lib.gui.window import Window

from . import Element


# Main

class Image(QLabel, Element):
    _pixmap: QPixmap

    def __init__(self, root: Window, src: str) -> None: ...

    def config(self) -> void: ...

    def Align(self, alignment: Qt.Alignment) -> Self: ...
