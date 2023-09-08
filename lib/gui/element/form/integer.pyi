from typing import TypeVar

from PyQt5.QtWidgets import QSpinBox

from lib import void
from lib.gui.element.form import FormControl
from lib.gui.window import Window

# Types

TIntegerInput = TypeVar("TIntegerInput", bound=IntegerInput)


# Main

class IntegerInput(QSpinBox, FormControl[int]):
    def __init__(self, root: Window, value: int) -> None: ...

    def config(self) -> void: ...

    def Min(self: TIntegerInput, value: int) -> TIntegerInput: ...

    def Max(self: TIntegerInput, value: int) -> TIntegerInput: ...
