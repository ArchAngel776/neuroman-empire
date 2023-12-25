from typing import Self

from PyQt5.QtGui import QFont


# Main

class Font(QFont):
    def Size(self, size: int) -> Self: ...

    def Bold(self, bold: bool = True) -> Self: ...

    def Italic(self, italic: bool = True) -> Self: ...

    def Underline(self, underline: bool = True) -> Self: ...
