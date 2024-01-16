from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.events.emitter import EventEmitter
from lib.gui.event import Event
from lib.gui.event.form_control_validated import FormControlValidated
from lib.gui.element.form import FormControl
from .validation import Validation

# Types

FormValidatorType = TypeVar("FormValidatorType")
FormValidatorValidationType = TypeVar("FormValidatorValidationType", bound=Validation)

TFormValidatorEmitValidationEvent = TypeVar("TFormValidatorEmitValidationEvent", bound=FormValidator)
FormValidatorEmitValidationEventType = TypeVar("FormValidatorEmitValidationEventType")
FormValidatorEmitValidationEventValidationType = TypeVar("FormValidatorEmitValidationEventValidationType", bound=Validation)


# Decorators

class EmitValidationEvent(
    Decorator[
        bool,
        [
            FormValidator[FormValidatorEmitValidationEventType, FormValidatorEmitValidationEventValidationType],
            FormValidatorEmitValidationEventType
        ]
    ],
    Generic[FormValidatorEmitValidationEventType, FormValidatorEmitValidationEventValidationType]
):
    def method(self, target: TFormValidatorEmitValidationEvent, value: FormValidatorEmitValidationEventType) -> bool: ...


# Main

class FormValidator(
    EventEmitter[Event.Type.Validated, FormControlValidated],
    ABC,
    Generic[FormValidatorType, FormValidatorValidationType]
):
    _validations: list[FormValidatorValidationType]

    _error_message: Optional[str]

    def __init__(self, *validations: FormValidatorValidationType) -> None: ...

    @method(EmitValidationEvent[FormValidatorType, FormValidatorValidationType])
    def validate(self, value: FormValidatorType) -> bool: ...

    @abstractmethod
    def bind(self, form_control: FormControl[FormValidatorType]) -> FormControl[FormValidatorType]: ...

    @property
    def error_message(self) -> Optional[str]: ...
