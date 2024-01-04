from lib.decorators import method
from lib.gui.element.form.validator.validation import Validation, ValidationMethod
from .data import UniqueValidationData


# Main

class Unique(Validation):
    def validate(self, target):
        if not self.match(target, self.data["collection"]):
            return False

        return True

    @staticmethod
    @method(ValidationMethod)
    def match(target, values):
        for value in values:
            if target == value:
                return False
        return True
