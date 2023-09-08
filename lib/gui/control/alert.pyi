from typing import TypeVar

from PyQt5.QtWidgets import QMessageBox

from lib.gui.control import ControlWindow

# Types

TAlert = TypeVar("TAlert", bound=Alert)


# Main

class Alert(ControlWindow):
    def __init__(self, text: str) -> None: ...

    def type(self: TAlert, icon: QMessageBox.Icon) -> TAlert: ...
