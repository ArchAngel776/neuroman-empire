from typing import TypeVar, Generic, Self

from lib.gui.element.form.select.v2.data import Select2Container
from lib.gui.element.form.select.v2.data.option import Select2Option

# Types

Select2GroupData = TypeVar("Select2GroupData")


# Main

class Select2Group(Generic[Select2GroupData]):
    _container: Select2Container[Select2GroupData]

    _group_id: str

    _name: str

    _options: list[Select2Option[Select2GroupData]]

    def __init__(self, container: Select2Container[Select2GroupData], group_id: str) -> None: ...

    def set_name(self, name: str) -> Self: ...

    def add_option(self, index: int, option: Select2Option[Select2GroupData]) -> Self: ...

    def remove_option(self, index: int) -> Self: ...

    def has(self, index: int) -> bool: ...

    @property
    def container(self) -> Select2Container[Select2GroupData]: ...

    @property
    def group_id(self) -> str: ...

    @property
    def name(self) -> str: ...

    @property
    def options(self) -> list[Select2Option[Select2GroupData]]: ...

    @property
    def index(self) -> int: ...

    def __getitem__(self, item: int) -> Select2Option[Select2GroupData]: ...

    def __len__(self) -> int: ...
