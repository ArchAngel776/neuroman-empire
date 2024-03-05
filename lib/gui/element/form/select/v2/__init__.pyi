from typing import Self, TypeVar, Generic, Optional

from PyQt5.QtGui import QShowEvent

from lib import void
from lib.gui.element.form import FormControl
from lib.gui.window import Window
from .base import QComboBox2

# Types

Select2BoxData = TypeVar("Select2BoxData")


# Main

class Select2Box(QComboBox2, FormControl[tuple[int, Optional[Select2BoxData]]], Generic[Select2BoxData]):
    def __init__(self, root: Window) -> None: ...

    def config(self) -> void: ...

    def showEvent(self, event: QShowEvent) -> void: ...

    def react(self, value: tuple[int, Optional[Select2BoxData]]) -> void: ...

    def select_event(self) -> void: ...

    def select_input(self) -> void: ...

    def Group(self, group_id: str, name: str) -> Self: ...

    def Option(self, group_id: str, title: str, data: Select2BoxData) -> Self: ...

    def Active(self, index: int) -> Self: ...
