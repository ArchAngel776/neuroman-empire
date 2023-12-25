from typing import TypeVar, Generic, Iterable, Callable, Optional, Self

from PyQt5.QtWidgets import QSizePolicy

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element import Element
from lib.gui.layout import Layout
from lib.gui.layout.type import LayoutType
from lib.gui.window import Window
from lib.helpers.gui_remover import GUIRemover

# Types

ListType = TypeVar("ListType")
ListTypeUpdateAfterRender = TypeVar("ListTypeUpdateAfterRender")
ListTypeClearLayout = TypeVar("ListTypeClearLayout")

TListUpdateAfterRender = TypeVar("TListUpdateAfterRender", bound=List)
TListClearLayout = TypeVar("TListClearLayout", bound=List)


# Decorators

class ClearLayout(
    Decorator[void, [List[ListTypeClearLayout]]],
    Generic[ListTypeClearLayout]
):
    _gui_remover: GUIRemover

    def __init__(self, original: Callable[[List[ListTypeClearLayout]], void]) -> None: ...

    def config(self, target: TListClearLayout) -> Self: ...


# Main

class List(Element, Generic[ListType]):
    _source_getter: Callable[[], Iterable[ListType]]

    _orientation: LayoutType

    _callback_builder: Callable[[ListType, Optional[int]], Layout] | None

    _sizing: QSizePolicy

    def __init__(self, root: Window, source_getter: Callable[[], Iterable[ListType]], orientation: LayoutType) -> None: ...

    def config(self) -> void: ...

    def InnerSizing(self, horizontal: QSizePolicy.Policy, vertical: QSizePolicy.Policy) -> Self: ...

    def Render(self, callback_builder: Callable[[ListType, Optional[int]], Layout]) -> Self: ...

    @method(ClearLayout[ListType])
    def update_list(self) -> void: ...

    @property
    def callback_builder(self) -> Callable[[ListType, Optional[int]], Layout]: ...
