from typing import TypeVar

from PyQt5.QtGui import QFont

# Types

TFont = TypeVar("TFont", bound=Font)


# Main

class Font(QFont):
    def Size(self: TFont, size: int) -> TFont: ...

    def Bold(self: TFont, bold: bool = True) -> TFont: ...

    def Italic(self: TFont, italic: bool = True) -> TFont: ...

    def Underline(self: TFont, underline: bool = True) -> TFont: ...
