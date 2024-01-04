from typing import TypeVar, Generic, Optional

from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtGui import QPaintEvent, QPen, QColor
from PyQt5.QtWidgets import QRubberBand

from lib import void
from lib.gui.element.form.validator.validation import Validation
from lib.gui.element.component.validation import ValidationField

# Types

ExceptionValidationFieldType = TypeVar("ExceptionValidationFieldType")
ExceptionValidationFieldValidationType = TypeVar("ExceptionValidationFieldValidationType", bound=Validation)


# Main

class ValidationException(QRubberBand, Generic[ExceptionValidationFieldType, ExceptionValidationFieldValidationType]):
    _field: ValidationField[ExceptionValidationFieldType, ExceptionValidationFieldValidationType]

    _text: str

    _pen: QPen

    _background_color: QColor

    _text_pen: QPen

    def __init__(
            self,
            field: ValidationField[ExceptionValidationFieldType, ExceptionValidationFieldValidationType]
    ) -> None: ...

    def config(self) -> void: ...

    def setup(self) -> void: ...

    def paintEvent(self, event: Optional[QPaintEvent]) -> void: ...

    def set_text(self, text: str) -> void: ...

    @property
    def position(self) -> QPoint: ...

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
    def text(self) -> str: ...
