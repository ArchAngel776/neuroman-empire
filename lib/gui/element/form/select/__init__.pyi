from typing import TypeVar, Generic, Self, Iterable

from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import QComboBox

from lib import void
from lib.gui.window import Window
from lib.gui.element.form import FormControl

# Types

SelectBoxData = TypeVar("SelectBoxData")


# Main

class SelectBox(QComboBox, FormControl[tuple[int, SelectBoxData]], Generic[SelectBoxData]):
    def __init__(self, root: Window) -> None: ...

    def config(self) -> void: ...

    def showEvent(self, event: QShowEvent) -> void: ...

    def react(self, value: tuple[int, SelectBoxData]) -> void: ...

    def select_event(self, index: int) -> void: ...

    def select_input(self, index: int) -> void: ...

    def Option(self, title: str, data: SelectBoxData) -> Self: ...

    def Active(self, index: int) -> Self: ...

    def Generate(self, source: Iterable[tuple[str, SelectBoxData]]) -> Self: ...
