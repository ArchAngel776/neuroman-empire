from typing import TypeVar, Generic, ClassVar

from PyQt5.QtCore import QObject, pyqtSignal

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.form import FormControl
from lib.gui.element.form.container import FormContainer
from lib.gui.element.form.validator.validation import Validation
from .control import FormElementControl

# Types

FormElementType = TypeVar("FormElementType")
FormElementValidationType = TypeVar("FormElementValidationType", bound=Validation)

TFormElementConfigControl = TypeVar("TFormElementConfigControl", bound=FormElement)
FormElementConfigControlType = TypeVar("FormElementConfigControlType")
FormElementConfigControlValidationType = TypeVar("FormElementConfigControlValidationType", bound=Validation)


# Decorators

class ConfigControl(
    Decorator[
        FormElementControl[FormElementConfigControlType], [
            FormElement[FormElementConfigControlType, FormElementConfigControlValidationType],
            FormControl[FormElementConfigControlType]
        ]
    ],
    Generic[FormElementConfigControlType, FormElementConfigControlValidationType]
):
    def method(
            self,
            target: TFormElementConfigControl,
            form_control: FormControl[FormElementConfigControlType]
    ) -> FormElementControl[FormElementConfigControlType]: ...


# Main

class FormElement(QObject, Generic[FormElementType, FormElementValidationType]):
    # Signals

    validation: ClassVar[pyqtSignal]
    update_validation: ClassVar[pyqtSignal]

    def __init__(self, container: FormContainer) -> None: ...

    @method(ConfigControl[FormElementType, FormElementValidationType])
    def Control(self, form_control: FormControl[FormElementType]) -> FormElementControl[FormElementType]: ...

    def validate(self) -> void: ...

    # Slots

    def send_validation_status(self, status: bool) -> void: ...
