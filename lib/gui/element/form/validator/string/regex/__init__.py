from re import match

from lib.decorators import method
from lib.gui.element.form.validator.validation import Validation, ValidationMethod


# Main

class Regex(Validation):
    def validate(self, target):
        if not self.match(target, self.data["pattern"]):
            return False

        return True

    @staticmethod
    @method(ValidationMethod)
    def match(target, value):
        return match(value, target) is not None
