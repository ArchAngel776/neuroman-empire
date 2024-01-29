from typing import TypeVar, Generic, ClassVar, Self

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

TFormElementConnectValidation = TypeVar("TFormElementConnectValidation", bound=FormElement)
FormElementConnectValidationType = TypeVar("FormElementConnectValidationType")
FormElementConnectValidationValidationType = TypeVar("FormElementConnectValidationValidationType", bound=Validation)

TFormElementConnectDestruction = TypeVar("TFormElementConnectDestruction", bound=FormElement)
FormElementConnectDestructionType = TypeVar("FormElementConnectDestructionType")
FormElementConnectDestructionValidationType = TypeVar("FormElementConnectDestructionValidationType", bound=Validation)


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


class ConnectValidation(
    Decorator[
        FormElementControl[FormElementConnectValidationType], [
            FormElement[FormElementConnectValidationType, FormElementConnectValidationValidationType],
            FormControl[FormElementConnectValidationType]
        ]
    ],
    Generic[FormElementConnectValidationType, FormElementConnectValidationValidationType]
):
    def method(
            self,
            target: TFormElementConnectValidation,
            form_control: FormControl[FormElementConnectValidationType]
    ) -> FormElementControl[FormElementConnectValidationType]: ...


class ConnectDestruction(
    Decorator[
        FormElementControl[FormElementConnectDestructionType], [
            FormElement[FormElementConnectDestructionType, FormElementConnectDestructionValidationType],
            FormControl[FormElementConnectDestructionType]
        ]
    ],
    Generic[FormElementConnectDestructionType, FormElementConnectDestructionValidationType]
):
    def config(
            self,
            target: TFormElementConnectDestruction,
            form_control: FormControl[FormElementConnectDestructionType]
    ) -> Self: ...


# Main

class FormElement(QObject, Generic[FormElementType, FormElementValidationType]):
    _container: FormContainer

    # Signals

    validation: ClassVar[pyqtSignal]
    update_validation: ClassVar[pyqtSignal]
    removed: ClassVar[pyqtSignal]

    def __init__(self, container: FormContainer) -> None: ...

    def config(self) -> void: ...

    @method(ConfigControl[FormElementType, FormElementValidationType])
    @method(ConnectValidation[FormElementType, FormElementValidationType])
    @method(ConnectDestruction[FormElementType, FormElementValidationType])
    def Control(self, form_control: FormControl[FormElementType]) -> FormElementControl[FormElementType]: ...

    def validate(self) -> void: ...

    def remove(self) -> void: ...

    # Slots

    def send_validation_status(self, status: bool) -> void: ...
