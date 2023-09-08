from PyQt5.QtWidgets import QMessageBox


# Main

class ControlWindow:
    def __init__(self, text):
        self._box = QMessageBox()
        self._box.setText(text)

    def title(self, title):
        self._box.setWindowTitle(title)
        return self

    def icon(self, icon):
        self._box.setWindowIcon(icon)
        return self

    def show(self):
        return self._box.exec_()
