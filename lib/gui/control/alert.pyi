from typing import Self

from PyQt5.QtWidgets import QMessageBox

from lib.gui.control import ControlWindow


# Main

class Alert(ControlWindow):
    def __init__(self, text: str) -> None: ...

    def type(self, icon: QMessageBox.Icon) -> Self: ...
