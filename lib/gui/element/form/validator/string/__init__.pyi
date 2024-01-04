from typing import Union

from lib.gui.element.form.validator import FormValidator
from lib.gui.layout.type import LayoutType
from lib.gui.window import Window
from lib.gui.element.component.validation import ValidationField
from lib.gui.element.form.text import TextInput
from .length import Length
from .regex import Regex

# Types

ValidationType = Union[Length, Regex]


# Main

class StringValidator(FormValidator[str, ValidationType]):
    def Widget(
            self,
            root: Window,
            form_control: TextInput,
            orientation: LayoutType
    ) -> ValidationField[str, ValidationType]: ...
