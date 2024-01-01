from typing import TypeVar, Self, Callable

from PyQt5.QtWidgets import QBoxLayout, QLayout

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element import Element
from lib.helpers.gui_remover import GUIRemover

# Types

TLayoutConfigElement = TypeVar("TLayoutConfigElement", bound=Layout)
TLayoutConditionalAdd = TypeVar("TLayoutConditionalAdd", bound=Layout)
TLayoutConditionalAppend = TypeVar("TLayoutConditionalAppend", bound=Layout)


# Decorators

class ConfigElement(Decorator[Layout, [Layout, Element]]):
    def config(self, target: TLayoutConfigElement, element: Element) -> Self: ...


class ConditionalAdd(Decorator[Layout, [Layout, Element]]):
    _gui_remover: GUIRemover

    def __init__(self, original: Callable[[Layout, Element], Layout]) -> None: ...

    def method(self, target: TLayoutConditionalAdd, element: Element, allow: bool = True) -> TLayoutConditionalAdd: ...


class ConditionalAppend(Decorator[Layout, [Layout, Layout, ...]]):
    _gui_remover: GUIRemover

    def __init__(self, original: Callable[[Layout, Layout, ...], Layout]) -> None: ...

    def method(self, target: TLayoutConditionalAppend, *layouts: Layout, allow: bool = True) -> TLayoutConditionalAppend: ...


# Main

class Layout:
    _layout: QBoxLayout
    _weight: int

    def __init__(self, layout: QBoxLayout) -> None: ...

    def weight(self, weight: int) -> Self: ...

    @method(ConditionalAdd)
    @method(ConfigElement)
    def add(self, element: Element) -> Self: ...

    @method(ConditionalAppend)
    def append(self, *layouts: Layout) -> Self: ...

    def stretch(self) -> Self: ...

    def constraint(self, constraint: QLayout.SizeConstraint) -> Self: ...

    def align(self, alignment: int) -> Self: ...

    def margin(self, horizontal: int, vertical: int) -> Self: ...

    def margin_horizontal(self, size: int) -> Self: ...

    def margin_vertical(self, size: int) -> Self: ...

    @property
    def element(self) -> QBoxLayout: ...

    def get_weight(self) -> int: ...
