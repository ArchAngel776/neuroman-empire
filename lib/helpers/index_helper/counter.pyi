from typing import Self

from PyQt5.QtCore import QModelIndex

from lib import void


# Main

class Counter:
    _position: int

    _index: QModelIndex

    def __init__(self) -> None: ...

    def increment_position(self) -> void: ...

    def setup(self, index: QModelIndex) -> Self: ...

    @property
    def position(self) -> int: ...

    @property
    def index(self) -> QModelIndex: ...
