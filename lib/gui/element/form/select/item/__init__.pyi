from typing import TypeVar, Generic, Optional

from .type import SelectItemType

# Types

SelectItemData = TypeVar("SelectItemData")


# Main

class SelectItem(Generic[SelectItemData]):
    _item_type: SelectItemType
    _data: Optional[SelectItemData]

    def __init__(self, item_type: SelectItemType, data: SelectItemData = None) -> None: ...

    @property
    def item_type(self) -> SelectItemType: ...

    @property
    def data(self) -> Optional[SelectItemData]: ...
