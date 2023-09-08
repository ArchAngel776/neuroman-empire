from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

from . import Element


# Main

class Image(QLabel, Element):
    def __init__(self, root, src):
        super().__init__(root)
        self._pixmap = QPixmap(src)

    def config(self):
        super().config()
        self.setPixmap(self._pixmap)

    def Align(self, alignment):
        self.setAlignment(alignment)
        return self
