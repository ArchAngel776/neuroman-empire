from typing import Self, TypeVar

from PyQt5.QtCore import QObject

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from .element import FormElement

# Types

TFormContainerNoRepeatUpdate = TypeVar("TFormContainerNoRepeatUpdate", bound=FormContainer)


# Decorators

class NoRepeatUpdate(Decorator[void, [FormContainer, bool]]):
    def method(self, target: TFormContainerNoRepeatUpdate, is_valid: bool) -> void: ...


# Main

class FormContainer(QObject):
    _elements: list[FormElement]

    _is_valid: bool

    def __init__(self) -> None: ...

    def add(self, element: FormElement) -> Self: ...

    def validate(self) -> void: ...

    # Slots

    @method(NoRepeatUpdate)
    def update_validation_status(self, is_valid: bool) -> void: ...

    @property
    def is_valid(self) -> bool: ...
