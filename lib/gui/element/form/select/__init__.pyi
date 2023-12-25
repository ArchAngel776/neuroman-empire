from typing import TypeVar, Generic, Optional, Self

from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import QComboBox

from lib import void
from lib.gui.element.form import FormControl
from lib.gui.window import Window

# Types

SelectBoxData = TypeVar("SelectBoxData")


# Main

class SelectBox(QComboBox, FormControl[tuple[int, Optional[SelectBoxData]]], Generic[SelectBoxData]):
    def __init__(self, root: Window) -> None: ...

    def config(self) -> void: ...

    def showEvent(self, event: QShowEvent) -> void: ...

    def react(self, value: tuple[int, Optional[SelectBoxData]]) -> void: ...

    def select_event(self, index: int) -> void: ...

    def select_input(self, index: int) -> void: ...

    def Group(self, title: str) -> Self: ...

    def Option(self, group: str, title: str, data: SelectBoxData = None) -> Self: ...

    def Active(self, index: int) -> Self: ...

    def V2(self, enabled: bool = True) -> Self: ...
