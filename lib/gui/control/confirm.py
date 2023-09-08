from PyQt5.QtWidgets import QMessageBox

from lib.gui.control import ControlWindow


# Main

class Confirm(ControlWindow):
    def __init__(self, text):
        super().__init__(text)
        self._box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
