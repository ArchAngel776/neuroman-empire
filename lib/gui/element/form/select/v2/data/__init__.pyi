from typing import TypeVar, Generic, Self

from .group import Select2Group

# Types

Select2ContainerData = TypeVar("Select2ContainerData")


# Main

class Select2Container(Generic[Select2ContainerData]):
    _groups: list[Select2Group[Select2ContainerData]]

    def __init__(self) -> None: ...

    def add_group(self, index: int, group: Select2Group[Select2ContainerData]) -> Self: ...

    def remove_group(self, index: int) -> Self: ...

    def has(self, index: int) -> bool: ...

    @property
    def groups(self) -> list[Select2Group[Select2ContainerData]]: ...

    def __getitem__(self, item: int) -> Select2Group[Select2ContainerData]: ...

    def __len__(self) -> int: ...
