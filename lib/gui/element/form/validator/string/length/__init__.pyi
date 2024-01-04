from lib.decorators import method
from lib.gui.element.form.validator.validation import Validation, ValidationMethod
from .data import LengthValidationData


# Main

class Length(Validation[str, LengthValidationData]):
    def validate(self, target: str) -> bool: ...

    @staticmethod
    @method(ValidationMethod[str, int])
    def min(target: str, value: int) -> bool: ...

    @staticmethod
    @method(ValidationMethod[str, int])
    def max(target: str, value: int) -> bool: ...

    @staticmethod
    @method(ValidationMethod[str, int])
    def length(target: str, value: int) -> bool: ...
