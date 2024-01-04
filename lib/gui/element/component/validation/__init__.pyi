from typing import TypeVar, Generic, Self

from PyQt5.QtCore import QPoint, QSize

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.component import Component
from lib.gui.element.form import FormControl
from lib.gui.element.form.validator import FormValidator
from lib.gui.element.form.validator.validation import Validation
from lib.gui.event.text_box_input_event import TextBoxInputEvent
from lib.gui.layout import Layout
from lib.gui.layout.type import LayoutType
from lib.gui.window import Window
from .container import ValidationContainer
from .exception import ValidationException

# Types

ValidationFieldType = TypeVar("ValidationFieldType")
ValidationFieldValidationType = TypeVar("ValidationFieldValidationType", bound=Validation)

TValidationFieldUpdateStyle = TypeVar("TValidationFieldUpdateStyle", bound=ValidationField)
ValidationFieldUpdateStyleType = TypeVar("ValidationFieldUpdateStyleType")
ValidationFieldUpdateStyleValidationType = TypeVar("ValidationFieldUpdateStyleValidationType", bound=Validation)


# Decorators

class UpdateStyle(
    Decorator[
        void, [
            ValidationField[ValidationFieldUpdateStyleType, ValidationFieldUpdateStyleValidationType],
            FormControl[ValidationFieldType]
        ]
    ],
    Generic[ValidationFieldUpdateStyleType, ValidationFieldUpdateStyleValidationType]
):
    def method(self, target: TValidationFieldUpdateStyle, control: FormControl[ValidationFieldType]) -> void: ...


# Main

class ValidationField(Component, Generic[ValidationFieldType, ValidationFieldValidationType]):
    class Watch(str):
        FORM_INPUT = ... #type: ValidationField.Watch

    _form_control: FormControl[ValidationFieldType]

    _validator: FormValidator[ValidationFieldType, ValidationFieldValidationType]

    _exception: ValidationException[ValidationFieldType, ValidationFieldValidationType]

    def __init__(
            self,
            root: Window,
            form_control: FormControl[ValidationFieldType],
            validator: FormValidator[ValidationFieldType, ValidationFieldValidationType],
            orientation: LayoutType
    ) -> None: ...

    def config(self) -> void: ...

    def validate(self, text: str) -> bool: ...

    def validate_input(self, event: TextBoxInputEvent) -> bool: ...

    def validate_container(self) -> bool: ...

    def Bind(self, container: ValidationContainer) -> Self: ...

    @method(UpdateStyle[ValidationFieldType, ValidationFieldValidationType])
    def set_exception(self, control: FormControl[ValidationFieldType]) -> void: ...

    @method(UpdateStyle[ValidationFieldType, ValidationFieldValidationType])
    def clear_exception(self, control: FormControl[ValidationFieldType]) -> void: ...

    def render_view(self, root: Window) -> Layout: ...

    @property
    def text(self) -> str: ...

    @property
    def position(self) -> QPoint: ...

    @property
    def size(self) -> QSize: ...
