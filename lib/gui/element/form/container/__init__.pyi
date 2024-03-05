from typing import Self, TypeVar, ClassVar, Any

from PyQt5.QtCore import QObject, pyqtSignal

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from .element import FormElement

# Types

TFormContainerConfigElement = TypeVar("TFormContainerConfigElement", bound=FormContainer)
TFormContainerConnectClose = TypeVar("TFormContainerConnectClose", bound=FormContainer)
TFormContainerNoRepeatUpdate = TypeVar("TFormContainerNoRepeatUpdate", bound=FormContainer)


# Decorators

class ConfigElement(Decorator[FormContainer, [FormContainer, FormElement[Any, Any]]]):
    def config(self, target: TFormContainerConfigElement, element: FormElement[Any, Any]) -> Self: ...


class ConnectClose(Decorator[FormContainer, [FormContainer, FormElement[Any, Any]]]):
    def config(self, target: TFormContainerConnectClose, element: FormElement[Any, Any]) -> Self: ...


class NoRepeatUpdate(Decorator[void, [FormContainer, bool]]):
    def method(self, target: TFormContainerNoRepeatUpdate, is_valid: bool) -> void: ...


# Main

class FormContainer(QObject):
    _elements: list[FormElement[Any, Any]]

    _is_valid: bool

    # Signals

    closed: ClassVar[pyqtSignal] = ...

    def __init__(self) -> None: ...

    @method(ConfigElement)
    @method(ConnectClose)
    def add(self, element: FormElement[Any, Any]) -> Self: ...

    def validate(self) -> void: ...

    def close(self) -> void: ...

    # Slots

    @method(NoRepeatUpdate)
    def update_validation_status(self, is_valid: bool) -> void: ...

    def remove_element(self, element: FormElement[Any, Any]) -> void: ...

    @property
    def is_valid(self) -> bool: ...
