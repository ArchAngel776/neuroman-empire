from enum import Enum
from typing import TypeVar, Generic, Optional, Self

from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import QRadioButton

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.form import FormControl
from lib.gui.layout import Layout
from lib.gui.layout.type import LayoutType
from lib.gui.window import Window

# Types

RadioButtonData = TypeVar("RadioButtonData", bound=Enum)

TRadioButtonToggleActive = TypeVar("TRadioButtonToggleActive", bound=Enum)
RadioButtonToggleActiveData = TypeVar("RadioButtonToggleActiveData", bound=Enum)


# Decorators

class ToggleActive(
    Decorator[void, [RadioButton[RadioButtonToggleActiveData, bool]]],
    Generic[RadioButtonToggleActiveData]
):
    def method(self, target: TRadioButtonToggleActive, selected: bool) -> void: ...


# Main

class RadioButton(FormControl[RadioButtonData], Generic[RadioButtonData]):
    _orientation: LayoutType

    _initial_value: Optional[RadioButtonData]

    _radios: dict[RadioButtonData, QRadioButton]

    def __init__(self, root: Window, orientation: LayoutType, initial_value: Optional[RadioButtonData] = ...) -> None: ...

    def config(self) -> void: ...

    def showEvent(self, event: QShowEvent) -> void: ...

    def react(self, value: RadioButtonData) -> void: ...

    def Add(self, value: RadioButtonData, label: Optional[str] = ...) -> Self: ...

    def createLayout(self) -> Layout: ...

    @property
    def selected(self) -> Optional[RadioButtonData]: ...

    # Slots

    @method(ToggleActive[RadioButtonData])
    def selectRadio(self) -> void: ...

    @method(ToggleActive[RadioButtonData])
    def selectInput(self) -> void: ...
