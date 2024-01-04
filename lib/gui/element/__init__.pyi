from typing import Self, TypeVar, Union, Callable, Any

from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtWidgets import QWidget, QSizePolicy

from lib import void
from lib.events.emitter import EventEmitter
from lib.gui.event import Event
from lib.gui.window import Window

# Types

TElement = TypeVar("TElement", bound=Element)

ElementEventListener = Union[
    Callable[[Element, QEvent], bool],
    Callable[[QEvent], bool],
    Callable[[Element], bool],
    Callable[[], bool]
]


# Main

class Element(QWidget, EventEmitter[Event.Type, Event]):
    def __init__(self, root: Window) -> None: ...

    def config(self) -> void: ...

    def event(self, event: Event) -> bool: ...

    def Name(self, name: str) -> Self: ...

    def Property(self, name: str, value: Any) -> Self: ...

    def Class(self, class_name: str | None) -> Self: ...

    def Sizing(self, horizontal: QSizePolicy.Policy, vertical: QSizePolicy.Policy) -> Self: ...

    def Width(self, width: int) -> Self: ...

    def MinWidth(self, width: int) -> Self: ...

    def MaxWidth(self, width: int) -> Self: ...

    def Height(self, height: int) -> Self: ...

    def MinHeight(self, height: int) -> Self: ...

    def MaxHeight(self, height: int) -> Self: ...

    def Hidden(self, hidden: bool = True) -> Self: ...

    def Font(self, font: QFont) -> Self: ...

    def Cursor(self, cursor: QCursor) -> Self: ...

    def ToolTip(self, tip: str) -> Self: ...

    def Margin(self, horizontal: int, vertical: int) -> Self: ...

    def On(
            self,
            event: Event.Type,
            callback: ElementEventListener,
            with_target: bool = True,
            with_event: bool = True
    ) -> Self: ...

    def update_style(self) -> void: ...

    @property
    def root(self) -> Window: ...
