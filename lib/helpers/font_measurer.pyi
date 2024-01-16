from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QFontMetrics


# Main

class FontMeasurer:
    def size(self, text: str, font: QFont) -> QSize: ...

    @staticmethod
    def metrics(font: QFont) -> QFontMetrics: ...
