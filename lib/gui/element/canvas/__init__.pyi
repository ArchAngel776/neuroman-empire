from typing import TypeVar, Generic

from PyQt5.QtGui import QPaintEvent

from lib import void
from lib.gui.element import Element
from lib.gui.window import Window

from .program import CanvasProgram

# Types

CanvasProgramType = TypeVar("CanvasProgramType", bound=CanvasProgram)


# Main

class Canvas(Element, Generic[CanvasProgramType]):
    _program: CanvasProgramType

    def __init__(self, root: Window, program: CanvasProgramType) -> None: ...

    def paintEvent(self, event: QPaintEvent) -> void: ...

    @property
    def program(self) -> CanvasProgramType: ...
