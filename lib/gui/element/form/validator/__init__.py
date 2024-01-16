from abc import ABC, abstractmethod

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.events.emitter import EventEmitter
from lib.gui.event import Event
from lib.gui.event.form_control_validated import FormControlValidated


# Decorators

class EmitValidationEvent(Decorator):
    def method(self, target, value):
        result = super().method(target, value)
        target.emit(Event.Type.Validated, FormControlValidated(result, target.error_message))
        return result


# Main

class FormValidator(EventEmitter, ABC):
    def __init__(self, *validations):
        super().__init__()
        self._validations = list(validations)
        self._error_message = None

    @method(EmitValidationEvent)
    def validate(self, value):
        for validation in self._validations:
            if not validation.validate(value):
                self._error_message = validation.error
                return False
        self._error_message = None
        return True

    @abstractmethod
    def bind(self, form_control):
        pass

    @property
    def error_message(self):
        return self._error_message
