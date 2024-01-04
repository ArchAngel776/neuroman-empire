from typing import NotRequired, Callable

from lib.gui.element.form.validator.data import ValidationData


# Main

class LengthValidationData(ValidationData):
    min: NotRequired[int | Callable[[], int]]
    max: NotRequired[int | Callable[[], int]]
    length: NotRequired[int | Callable[[], int]]
