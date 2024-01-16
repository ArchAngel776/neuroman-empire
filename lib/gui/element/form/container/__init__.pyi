from typing import Self

from PyQt5.QtCore import QObject

from lib import void
from .element import FormElement


# Main

class FormContainer(QObject):
    _elements: list[FormElement]

    _is_valid: bool

    def __init__(self) -> None: ...

    def add(self, element: FormElement) -> Self: ...

    def validate(self) -> void: ...

    # Slots

    def update_validation_status(self, is_valid: bool) -> void: ...

    @property
    def is_valid(self) -> bool: ...
