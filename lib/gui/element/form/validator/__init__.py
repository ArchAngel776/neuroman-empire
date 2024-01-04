from abc import ABC, abstractmethod


# Main

class FormValidator(ABC):
    def __init__(self, *validations):
        self._validations = list(validations)
        self._error_message = None

    def validate(self, target):
        for validation in self._validations:
            if not validation.validate(target):
                self._error_message = validation.error
                return False
        self._error_message = None
        return True

    @abstractmethod
    def Widget(self, root, form_control, orientation):
        pass

    @property
    def error_message(self):
        return self._error_message
