from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, Self

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element import Element
from lib.gui.window import Window

# Types

FormInputType = TypeVar("FormInputType")

FormControlType = TypeVar("FormControlType")

TFormUpdateControlControl = TypeVar("TFormUpdateControlControl", bound=FormInput)
FormUpdateControlType = TypeVar("FormUpdateControlType")

TFormControlExistsInput = TypeVar("TFormControlExistsInput", bound=FormControl)
FormExistsControlType = TypeVar("FormExistsControlType")


# Decorators

class UpdateControl(
    Decorator[void, [FormInput[FormUpdateControlType], FormUpdateControlType, bool]],
    Generic[FormUpdateControlType]
):
    def method(
            self,
            target: TFormUpdateControlControl,
            value: FormUpdateControlType,
            update_control: bool = True
    ) -> void: ...


class ExistsInput(
    Decorator[void, [FormControl[FormExistsControlType], FormExistsControlType]],
    Generic[FormExistsControlType]
):
    def method(self, target: TFormControlExistsInput, value: FormExistsControlType) -> void: ...


# Meta

class FormControlMeta(type(Element), type(ABC)): ...


# Data

class FormInput(Generic[FormInputType]):
    _value: FormInputType
    _form_control: Optional[FormControl[FormInputType]]

    def __init__(self, value: FormInputType) -> None: ...

    def bind(self, form_control: FormControl[FormInputType]) -> Self: ...

    @method(UpdateControl[FormInputType])
    def update(self, value: FormInputType) -> void: ...

    @property
    def value(self) -> FormInputType: ...

    @property
    def form_control(self) -> Optional[FormControl[FormInputType]]: ...


# Main

class FormControl(Element, ABC, Generic[FormControlType], metaclass=FormControlMeta):
    _form_input: Optional[FormInput[FormControlType]]

    def __init__(self, root: Window) -> None: ...

    def Bind(self, form_input: FormInput[FormControlType]) -> Self: ...

    @abstractmethod
    def react(self, value: FormControlType) -> void: ...

    @method(ExistsInput[FormControlType])
    def input(self, value: FormControlType) -> void: ...

    def has_form_input(self) -> bool: ...

    @property
    def value(self) -> FormControlType: ...
