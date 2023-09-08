from typing import Generic, TypeVar

from lib.gui.event import Event

# Types

SelectBoxData = TypeVar("SelectBoxData")


# Main

class SelectBoxSelectedEvent(Event, Generic[SelectBoxData]):
    _title: str
    _data: SelectBoxData

    def __init__(self, title: str, data: SelectBoxData) -> None: ...

    @property
    def title(self) -> str: ...

    @property
    def data(self) -> SelectBoxData: ...
