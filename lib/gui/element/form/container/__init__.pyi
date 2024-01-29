from typing import Self, TypeVar

from PyQt5.QtCore import QObject

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from .element import FormElement

# Types

TFormContainerConfigElement = TypeVar("TFormContainerConfigElement", bound=FormContainer)
TFormContainerNoRepeatUpdate = TypeVar("TFormContainerNoRepeatUpdate", bound=FormContainer)


# Decorators

class ConfigElement(Decorator[FormContainer, [FormContainer, FormContainer]]):
    def config(self, target: TFormContainerConfigElement, element: FormElement) -> Self: ...


class NoRepeatUpdate(Decorator[void, [FormContainer, bool]]):
    def method(self, target: TFormContainerNoRepeatUpdate, is_valid: bool) -> void: ...


# Main

class FormContainer(QObject):
    _elements: list[FormElement]

    _is_valid: bool

    def __init__(self) -> None: ...

    @method(ConfigElement)
    def add(self, element: FormElement) -> Self: ...

    def validate(self) -> void: ...

    # Slots

    @method(NoRepeatUpdate)
    def update_validation_status(self, is_valid: bool) -> void: ...

    def remove_element(self, element: FormElement) -> void: ...

    @property
    def is_valid(self) -> bool: ...
