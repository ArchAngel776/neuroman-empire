from typing import TypeVar, Union, Callable

from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtWidgets import QWidget, QSizePolicy

from lib import void
from lib.events.emitter import EventEmitter
from lib.gui.event import Event
from lib.gui.window import Window

# Types

TElement = TypeVar("TElement", bound=Element)

ElementEventListener = Union[
    Callable[[Element, Event], bool],
    Callable[[Event], bool],
    Callable[[Element], bool]
]


# Main

class Element(QWidget, EventEmitter[Event.Type, Event]):
    def __init__(self, root: Window) -> None: ...

    def config(self) -> void: ...

    def event(self, event: Event) -> bool: ...

    def Name(self: TElement, name: str) -> TElement: ...

    def Class(self: TElement, class_name: str) -> TElement: ...

    def Sizing(self: TElement, horizontal: QSizePolicy.Policy, vertical: QSizePolicy.Policy) -> TElement: ...

    def Width(self: TElement, width: int) -> TElement: ...

    def MinWidth(self: TElement, width: int) -> TElement: ...

    def MaxWidth(self: TElement, width: int) -> TElement: ...

    def Height(self: TElement, height: int) -> TElement: ...

    def MinHeight(self: TElement, height: int) -> TElement: ...

    def MaxHeight(self: TElement, height: int) -> TElement: ...

    def Font(self: TElement, font: QFont) -> TElement: ...

    def Cursor(self: TElement, cursor: QCursor) -> TElement: ...

    def ToolTip(self: TElement, tip: str) -> TElement: ...

    def Margin(self: TElement, horizontal: int, vertical: int) -> TElement: ...

    def On(
            self: TElement,
            event: Event.Type,
            callback: ElementEventListener,
            with_target: bool = True,
            with_event: bool = True
    ) -> TElement: ...

    @property
    def root(self) -> Window: ...
