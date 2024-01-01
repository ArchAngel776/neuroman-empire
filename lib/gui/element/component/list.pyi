from typing import TypeVar, Generic, Iterable, Callable, Optional, Self

from lib import void
from lib.gui.element.component import Component
from lib.gui.layout import Layout
from lib.gui.layout.type import LayoutType
from lib.gui.window import Window

# Types

ListType = TypeVar("ListType")


# Main

class List(Component, Generic[ListType]):
    _source_getter: Callable[[], Iterable[ListType]]

    _callback_builder: Callable[[ListType, Optional[int]], Layout] | None

    def __init__(self, root: Window, source_getter: Callable[[], Iterable[ListType]], orientation: LayoutType) -> None: ...

    def config(self) -> void: ...

    def Render(self, callback_builder: Callable[[ListType, Optional[int]], Layout]) -> Self: ...

    def render_view(self) -> Layout: ...

    def render_item(self, data: tuple[int, Layout]): ...

    @property
    def callback_builder(self) -> Callable[[ListType, Optional[int]], Layout]: ...
