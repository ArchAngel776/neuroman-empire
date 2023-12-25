from typing import Self

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

# Types

ControlCode = int


# Main

class ControlWindow:
    _box: QMessageBox

    def __init__(self, text: str) -> None: ...

    def title(self, title: str) -> Self: ...

    def icon(self, icon: QIcon) -> Self: ...

    def show(self) -> ControlCode: ...
