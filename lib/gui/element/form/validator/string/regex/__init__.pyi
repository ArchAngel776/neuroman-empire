from lib.decorators import method
from lib.gui.element.form.validator.validation import Validation, ValidationMethod
from .data import RegexValidationData


# Main

class Regex(Validation[str, RegexValidationData]):
    def validate(self, target: str) -> bool: ...

    @staticmethod
    @method(ValidationMethod[str, str])
    def match(target: str, value: str) -> bool: ...
