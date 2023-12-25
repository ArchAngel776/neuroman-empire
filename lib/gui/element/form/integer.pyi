from typing import Self

from PyQt5.QtWidgets import QSpinBox

from lib import void
from lib.gui.element.form import FormControl
from lib.gui.window import Window


# Main

class IntegerInput(QSpinBox, FormControl[int]):
    def __init__(self, root: Window, value: int) -> None: ...

    def config(self) -> void: ...

    def react(self, value: int) -> void: ...

    def Min(self, value: int) -> Self: ...

    def Max(self, value: int) -> Self: ...
