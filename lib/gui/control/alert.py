from PyQt5.QtWidgets import QMessageBox

from lib.gui.control import ControlWindow


# Main

class Alert(ControlWindow):
    def __init__(self, text):
        super().__init__(text)
        self._box.setStandardButtons(QMessageBox.Ok)

    def type(self, icon):
        self._box.setIcon(icon)
        return self
