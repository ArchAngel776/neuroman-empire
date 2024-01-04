from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Callable

from lib.decorators.decorator import Decorator
from lib.gui.element.form.validator.data import ValidationData

# Types

ValidationType = TypeVar("ValidationType")
ValidationDataType = TypeVar("ValidationDataType", bound=ValidationData)

ValidationMethodType = TypeVar("ValidationMethodType")
ValidationMethodValue = TypeVar("ValidationMethodValue")


# Decorators

class ValidationMethod(
    Decorator[bool, [ValidationMethodType, ValidationMethodValue | Callable[[], ValidationMethodValue]]],
    Generic[ValidationMethodType, ValidationMethodValue]
):
    def method(self, target: ValidationMethodType, value: ValidationMethodValue) -> bool: ...


# Main

class Validation(ABC, Generic[ValidationType, ValidationDataType]):
    _data: ValidationDataType

    def __init__(self, data: ValidationDataType) -> None: ...

    @abstractmethod
    def validate(self, target: ValidationType) -> bool: ...

    @property
    def data(self) -> ValidationDataType: ...

    @property
    def error(self) -> str: ...
