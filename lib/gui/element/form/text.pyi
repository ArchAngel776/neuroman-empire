from typing import TypeVar

from PyQt5.QtWidgets import QLineEdit

from lib import void
from lib.gui.element.form import FormControl
from lib.gui.window import Window

# Types

TTextInput = TypeVar("TTextInput", bound=TextInput)


# Main

class TextInput(QLineEdit, FormControl[str]):
    def __init__(self, root: Window, value: str) -> None: ...

    def config(self) -> void: ...

    def Length(self: TTextInput, length: int) -> TTextInput: ...
