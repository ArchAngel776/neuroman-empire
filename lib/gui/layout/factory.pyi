from PyQt5.QtWidgets import QBoxLayout

from lib.gui.layout import Layout
from lib.gui.layout.type import LayoutType


# Main

class LayoutFactory:
    _layout_type: LayoutType

    def __init__(self, layout_type: LayoutType) -> None: ...

    @property
    def layout(self) -> QBoxLayout: ...

    def create(self) -> Layout: ...
