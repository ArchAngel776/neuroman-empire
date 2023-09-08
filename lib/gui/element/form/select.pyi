from typing import TypeVar, Generic, Optional

from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import QComboBox

from lib import void
from lib.gui.element.form import FormControl

# Types

TSelectBox = TypeVar("TSelectBox", bound=SelectBox)
SelectBoxData = TypeVar("SelectBoxData")


# Main

class SelectBox(QComboBox, FormControl[tuple[int, Optional[SelectBoxData]]], Generic[SelectBoxData]):
    def config(self) -> void: ...

    def showEvent(self, event: QShowEvent) -> void: ...

    def select_event(self, index: int) -> void: ...

    def select_input(self, index: int) -> void: ...

    def Option(self: TSelectBox, title: str, data: SelectBoxData = None) -> TSelectBox: ...

    def Active(self: TSelectBox, index: int) -> TSelectBox: ...
