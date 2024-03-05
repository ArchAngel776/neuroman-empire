from typing import TypeVar, Generic, Optional, Self

from lib.gui.element.form.select.v2.data.group import Select2Group

# Types

Select2OptionData = TypeVar("Select2OptionData")


# Main

class Select2Option(Generic[Select2OptionData]):
    _group: Select2Group[Select2OptionData]

    _title: str

    _data: Optional[Select2OptionData]

    def __init__(self, group: Select2Group[Select2OptionData]) -> None: ...

    def set_title(self, title: str) -> Self: ...

    def set_data(self, data: Optional[Select2OptionData]) -> Self: ...

    @property
    def group(self) -> Select2Group[Select2OptionData]: ...

    @property
    def title(self) -> str: ...

    @property
    def data(self) -> Optional[Select2OptionData]: ...

    @property
    def index(self) -> int: ...
