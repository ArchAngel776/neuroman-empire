from enum import Enum
from typing import Generic, TypeVar

from lib.gui.event import Event

# Types

RadioButtonData = TypeVar("RadioButtonData", bound=Enum)


# Main

class RadioButtonToggled(Event, Generic[RadioButtonData]):
    _value: RadioButtonData

    def __init__(self, value: RadioButtonData) -> None: ...

    @property
    def value(self) -> RadioButtonData: ...