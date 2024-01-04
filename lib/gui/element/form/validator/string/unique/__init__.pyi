from lib.decorators import method
from lib.gui.element.form.validator.validation import Validation, ValidationMethod
from .data import UniqueValidationData


# Main

class Unique(Validation[str, UniqueValidationData]):
    def validate(self, target: str) -> bool: ...

    @staticmethod
    @method(ValidationMethod[str, list[str]])
    def match(target: str, values: list[str]) -> bool: ...
