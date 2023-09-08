from typing import TypeVar

from PyQt5.QtWidgets import QBoxLayout, QLayout

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element import Element

# Types

TLayout = TypeVar("TLayout", bound=Layout)
TLayoutConfig = TypeVar("TLayoutConfig", bound=Layout)


# Decorators

class ConfigElement(Decorator[Layout, [Layout, Element]]):
    def config(self, target: TLayoutConfig, element: Element) -> ConfigElement: ...


# Main

class Layout:
    _layout: QBoxLayout
    _weight: int

    def __init__(self, layout: QBoxLayout) -> None: ...

    def weight(self: TLayout, weight: int) -> TLayout: ...

    @method(ConfigElement)
    def add(self: TLayout, element: Element) -> TLayout: ...

    def append(self: TLayout, layout: Layout) -> TLayout: ...

    def stretch(self: TLayout) -> TLayout: ...

    def constraint(self: TLayout, constraint: QLayout.SizeConstraint) -> TLayout: ...

    def align(self: TLayout, alignment: int) -> TLayout: ...

    def margin(self: TLayout, horizontal: int, vertical: int) -> TLayout: ...

    def margin_horizontal(self: TLayout, size: int) -> TLayout: ...

    def margin_vertical(self: TLayout, size: int) -> TLayout: ...

    @property
    def element(self) -> QBoxLayout: ...

    def get_weight(self) -> int: ...
