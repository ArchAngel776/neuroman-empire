from lib.decorators import method
from lib.gui.element.form.validator.validation import Validation, ValidationMethod
from .data import LengthValidationData


# Main

class Length(Validation):
    def validate(self, target):
        if not self.min(target, self.data["min"]):
            return False

        if not self.max(target, self.data["max"]):
            return False

        if not self.length(target, self.data["length"]):
            return False

        return True

    @staticmethod
    @method(ValidationMethod)
    def min(target, value):
        return len(target) >= value

    @staticmethod
    @method(ValidationMethod)
    def max(target, value):
        return len(target) <= value

    @staticmethod
    @method(ValidationMethod)
    def length(target, value):
        return len(target) == value
