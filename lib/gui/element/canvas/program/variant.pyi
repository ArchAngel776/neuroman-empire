from abc import abstractmethod, ABC
from typing import Generic, TypeVar

from PyQt5.QtGui import QPainter

from lib import void
from lib.gui.element.canvas.program import CanvasProgram

# Types

CanvasProgramType = TypeVar("CanvasProgramType", bound=CanvasProgram)


# Main

class CanvasProgramVariant(ABC, Generic[CanvasProgramType]):
    _program: CanvasProgramType

    def __init__(self, program: CanvasProgramType) -> None: ...

    @abstractmethod
    def draw(self, painter: QPainter) -> void: ...

    @property
    def program(self) -> CanvasProgramType: ...
