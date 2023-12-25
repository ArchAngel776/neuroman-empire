from typing import Optional

from PyQt5.QtCore import QSize


# Main

class Sizer:
    _min: QSize
    _max: Optional[QSize]

    def __init__(self, min_width: int, min_height: int, max_width: int = None, max_height: int = None) -> None: ...
    @property
    def min(self) -> QSize: ...

    @property
    def max(self) -> QSize: ...
