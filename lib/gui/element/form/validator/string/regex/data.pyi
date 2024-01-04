from typing import NotRequired, Callable

from lib.gui.element.form.validator.data import ValidationData


# Main

class RegexValidationData(ValidationData):
    pattern: NotRequired[str | Callable[[], str]]
