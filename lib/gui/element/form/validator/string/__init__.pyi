from typing import Union

from lib.gui.element.form.text import TextInput
from lib.gui.element.form.validator import FormValidator
from lib.gui.event.text_box_input_event import TextBoxInputEvent
from .length import Length
from .regex import Regex

# Types

StringValidationType = Union[Length, Regex]


# Main

class StringValidator(FormValidator[str, StringValidationType]):
    def bind(self, form_control: TextInput) -> TextInput: ...

    def validate_text_input(self, event: TextBoxInputEvent) -> bool: ...
