from typing import TypeVar, Generic, Self, Optional

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPen, QColor, QPaintEvent, QPainterPath
from PyQt5.QtWidgets import QRubberBand

from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormControl
from lib.helpers.font_measurer import FontMeasurer

# Types

ValidatorType = TypeVar("ValidatorType")


# Main

class ValidatorException(QRubberBand, Generic[ValidatorType]):
    _message: str

    _font_measurer: FontMeasurer

    _left_side: bool

    def __init__(self) -> None: ...

    def prepare(self, form_control: FormControl[ValidatorType]) -> Self: ...

    def setMessage(self, message: str) -> Self: ...

    def open(self) -> void: ...

    def close(self) -> void: ...

    def paintEvent(self, event: Optional[QPaintEvent]) -> void: ...

    def from_left_side(self, path: QPainterPath) -> QPainterPath: ...

    def from_right_side(self, path: QPainterPath) -> QPainterPath: ...

    @property
    def message(self) -> str: ...

    @property
    def size(self) -> QSize: ...

    @property
    def arrow_side(self) -> int: ...

    @property
    def arrow_height(self) -> int: ...

    @property
    def stroke(self) -> int: ...

    @property
    def radius(self) -> int: ...

    @property
    def padding(self) -> int: ...

    @property
    def text_color(self) -> QColor: ...

    @property
    def stroke_color(self) -> QColor: ...

    @property
    def background_color(self) -> QColor: ...

    @property
    def pen(self) -> QPen: ...

    @property
    def text_pen(self) -> QPen: ...

    @property
    def text_font(self) -> Font: ...
