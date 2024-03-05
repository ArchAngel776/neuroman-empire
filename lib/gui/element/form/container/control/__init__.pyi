from typing import TypeVar, Generic, ClassVar, Self

from PyQt5.QtCore import QObject, pyqtSignal

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.form import FormControl
from lib.gui.element.form.validator import FormValidator
from lib.gui.element.form.validator.validation import Validation
from lib.gui.event.form_control_validated import FormControlValidated
from lib.gui.element.form.container.element import FormElement
from .exception import ValidatorException

# Types

FormElementControlType = TypeVar("FormElementControlType")
FormElementControlValidationType = TypeVar("FormElementControlValidationType", bound=Validation)

TFormElementControlFocusOn = TypeVar("TFormElementControlFocusOn", bound=FormElementControl)
FormElementControlFocusOnType = TypeVar("FormElementControlFocusOnType")
FormElementControlFocusOnValidationType = TypeVar("FormElementControlFocusOnValidationType", bound=Validation)

TFormElementControlUpdateStyle = TypeVar("TFormElementControlUpdateStyle", bound=FormElementControl)
FormElementControlUpdateStyleType = TypeVar("FormElementControlUpdateStyleType")
FormElementControlUpdateStyleValidationType = TypeVar("FormElementControlUpdateStyleValidationType", bound=Validation)


# Decorators

class FocusOn(
    Decorator[
        bool, [
            FormElementControl[FormElementControlFocusOnType, FormElementControlFocusOnValidationType],
            FormControlValidated
        ]
    ],
    Generic[FormElementControlFocusOnType, FormElementControlFocusOnValidationType]
):
    def config(self, target: TFormElementControlFocusOn, event: FormControlValidated) -> Self: ...


class UpdateStyle(
    Decorator[
        bool, [
            FormElementControl[FormElementControlUpdateStyleType, FormElementControlUpdateStyleValidationType],
            FormControlValidated
        ]
    ],
    Generic[FormElementControlUpdateStyleType, FormElementControlUpdateStyleValidationType]
):
    def method(self, target: TFormElementControlUpdateStyle, event: FormControlValidated) -> bool: ...


# Main

class FormElementControl(QObject, Generic[FormElementControlType, FormElementControlValidationType]):
    _form_control: FormControl[FormElementControlType]

    _exception: ValidatorException[FormElementControlType]

    # Signals

    validation: ClassVar[pyqtSignal] = ...
    validate: ClassVar[pyqtSignal] = ...

    def __init__(self, form_control: FormControl[FormElementControlType]) -> None: ...

    def config(self, element: FormElement[FormElementControlType, FormElementControlValidationType]) -> void: ...

    def Validator(
            self,
            validator: FormValidator[FormElementControlType, FormElementControlValidationType]
    ) -> FormControl[FormElementControlType]: ...

    @method(FocusOn[FormElementControlType, FormElementControlValidationType])
    @method(UpdateStyle[FormElementControlType, FormElementControlValidationType])
    def on_validate(self, event: FormControlValidated) -> bool: ...

    # Slots

    def make_validation(self) -> void: ...

    def hide_message(self) -> void: ...

    @property
    def form_control(self) -> FormControl[FormElementControlType]: ...