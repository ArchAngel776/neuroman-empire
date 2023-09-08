from PyQt5.QtWidgets import QPushButton

from lib import void
from lib.gui.element import Element
from lib.gui.window import Window


# Main

class Button(QPushButton, Element):
    def __init__(self, root: Window, text: str) -> None: ...

    def config(self) -> void: ...

    def click_event(self) -> void: ...
