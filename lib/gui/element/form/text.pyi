from typing import Self

from PyQt5.QtWidgets import QLineEdit

from lib import void
from lib.gui.element.form import FormControl
from lib.gui.window import Window


# Main

class TextInput(QLineEdit, FormControl[str]):
    def __init__(self, root: Window, value: str) -> None: ...

    def config(self) -> void: ...

    def react(self, value: str) -> void: ...

    def Length(self, length: int) -> Self: ...

    def input_event(self, text: str) -> void: ...
