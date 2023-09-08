from typing import TypeVar

from PyQt5.QtWidgets import QDoubleSpinBox

from lib import void
from lib.gui.element.form import FormControl
from lib.gui.window import Window

# Types

TNumberInput = TypeVar("TNumberInput", bound=NumberInput)


# Main

class NumberInput(QDoubleSpinBox, FormControl[float]):
    def __init__(self, root: Window, value: float) -> None: ...

    def config(self) -> void: ...

    def Min(self: TNumberInput, value: float) -> TNumberInput: ...

    def Max(self: TNumberInput, value: float) -> TNumberInput: ...

    def Precision(self: TNumberInput, precision: int) -> TNumberInput: ...
