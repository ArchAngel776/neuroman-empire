from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QLabel

from lib.hooks import palette_color
from lib.gui.element import Element


# Main

class Text(QLabel, Element):
    def __init__(self, root, text):
        super().__init__(root)
        self.setText(text)

    def Color(self, color):
        self.setPalette(palette_color(QPalette.WindowText, color))
        return self

    def Align(self, alignment):
        self.setAlignment(alignment)
        return self

    def Wrap(self):
        self.setWordWrap(True)
        return self
