from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import QCheckBox

from lib import void
from lib.gui.element.form import FormControl
from lib.gui.window import Window


# Main

class CheckBox(QCheckBox, FormControl[bool]):
    def __init__(self, root: Window, checked: bool) -> None: ...

    def config(self) -> void: ...

    def showEvent(self, event: QShowEvent) -> void: ...

    def change_event(self) -> void: ...

    def change_input(self) -> void: ...
