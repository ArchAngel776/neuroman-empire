from typing import Generic, TypeVar, Optional

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element import Element
from lib.gui.window import Window

# Types

TFormControl = TypeVar("TFormControl", bound=FormControl)
FormType = TypeVar("FormType")

FormControlType = TypeVar("FormControlType")

TFormControlExistsInput = TypeVar("TFormControlExistsInput", bound=FormControl)
FormExistsInputType = TypeVar("FormExistsInputType")


# Decorators

class ExistsInput(
    Decorator[void, [FormControl[FormExistsInputType], FormExistsInputType]],
    Generic[FormExistsInputType]
):
    def method(self, target: TFormControlExistsInput, value: FormExistsInputType) -> void: ...


# Data

class FormInput(Generic[FormType]):
    _value: FormType

    def __init__(self, value: FormType): ...

    def update(self, value: FormType) -> void: ...

    @property
    def value(self) -> FormType: ...


# Main

class FormControl(Element, Generic[FormControlType]):
    _form_input: Optional[FormInput[FormControlType]]

    def __init__(self, root: Window) -> None:

    def Bind(self: TFormControl, form_input: FormInput[FormControlType]) -> TFormControl: ...

    @method(ExistsInput[FormControlType])
    def input(self, value: FormControlType) -> void: ...

    def has_form_input(self) -> bool: ...
