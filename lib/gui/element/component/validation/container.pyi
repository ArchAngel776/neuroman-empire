from typing import Any

from lib import void
from lib.gui.element.component.validation import ValidationField


# Main

class ValidationContainer:
    _validation_fields: list[ValidationField[Any, Any]]

    def __init__(self) -> None: ...

    def register_field(self, validation_field: ValidationField[Any, Any]) -> void: ...

    def validate(self) -> bool: ...

    @property
    def validation_fields(self) -> list[ValidationField[Any, Any]]: ...
