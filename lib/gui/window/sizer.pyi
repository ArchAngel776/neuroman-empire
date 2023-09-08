from PyQt5.QtCore import QSize


# Main

class Sizer:
    _min: QSize
    _max: QSize

    def __init__(self, min_width: int, min_height: int, max_width: int, max_height: int) -> None: ...
    @property
    def min(self) -> QSize: ...

    @property
    def max(self) -> QSize: ...
