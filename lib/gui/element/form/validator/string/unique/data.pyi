from typing import NotRequired, Callable

from lib.gui.element.form.validator.data import ValidationData


# Main

class UniqueValidationData(ValidationData):
    collection: NotRequired[list[str] | Callable[[], list[str]]]
