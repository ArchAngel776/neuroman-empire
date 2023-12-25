from typing import Generic, TypeVar, Optional, Self, Iterator

# Types

SelectModelGroupData = TypeVar("SelectModelGroupData")


# Main

class SelectModelGroup(Generic[SelectModelGroupData]):
    _name: str

    _items: list[tuple[str, Optional[SelectModelGroupData]]]

    def __init__(self) -> None: ...

    def setName(self, name: str) -> Self: ...

    def add(self, title: str, data: SelectModelGroupData = None) -> Self: ...

    @property
    def name(self) -> str: ...

    def __getitem__(self, index: int) -> tuple[str, Optional[SelectModelGroupData]]: ...

    def __len__(self) -> int: ...

    def __iter__(self) -> Iterator[tuple[str, Optional[SelectModelGroupData]]]: ...
