from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

from lib.gui.window import Window
from lib.gui.layout.type import LayoutType
from lib.gui.element.form import FormControl
from lib.gui.element.component.validation import ValidationField
from .validation import Validation

# Types

FormValidatorType = TypeVar("FormValidatorType")
FormValidatorValidationType = TypeVar("FormValidatorValidationType", bound=Validation)


# Main

class FormValidator(ABC, Generic[FormValidatorType, FormValidatorValidationType]):
    _validations: list[FormValidatorValidationType]

    _error_message: Optional[str]

    def __init__(self, *validations: FormValidatorValidationType) -> None: ...

    def validate(self, target: FormValidatorType) -> bool: ...

    @abstractmethod
    def Widget(
            self,
            root: Window,
            form_control: FormControl[FormValidatorType],
            orientation: LayoutType
    ) -> ValidationField[FormValidatorType, FormValidatorValidationType]: ...

    @property
    def error_message(self) -> Optional[str]: ...
