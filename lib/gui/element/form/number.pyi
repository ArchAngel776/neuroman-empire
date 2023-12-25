from typing import Self

from PyQt5.QtWidgets import QDoubleSpinBox

from lib import void
from lib.gui.element.form import FormControl
from lib.gui.window import Window


# Main

class NumberInput(QDoubleSpinBox, FormControl[float]):
    def __init__(self, root: Window, value: float) -> None: ...

    def config(self) -> void: ...

    def react(self, value: float) -> void: ...

    def Min(self, value: float) -> Self: ...

    def Max(self, value: float) -> Self: ...

    def Precision(self, precision: int) -> Self: ...
