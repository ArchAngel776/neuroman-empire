from typing import TypeVar

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

# Types

TControlWindow = TypeVar("TControlWindow", bound=ControlWindow)


# Main

class ControlWindow:
    _box: QMessageBox

    def __init__(self, text: str) -> None: ...

    def title(self: TControlWindow, title: str) -> TControlWindow: ...

    def icon(self: TControlWindow, icon: QIcon) -> TControlWindow: ...

    def show(self) -> int: ...
