from abc import ABC, abstractmethod
from typing import Self, Callable, TypeVar

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

TComponentClearRender = TypeVar("TComponentClearRender", bound=Component)


# Decorators

class ClearRender(Decorator[void, [Component]]):
    _remover: GUIRemover

    def __init__(self, original: Callable[[Component], void]) -> None: ...

    def config(self, target: TComponentClearRender) -> Self: ...


# Meta

class ComponentMeta(type(Element), type(ABC)): ...


# Main

class Component(Element, ABC, metaclass=ComponentMeta):
    _orientation: LayoutType
    _sizing: QSizePolicy

    def __init__(self, root: Window, orientation: LayoutType) -> None: ...

    def config(self) -> void: ...

    def InnerSizing(self, horizontal: QSizePolicy.Policy, vertical: QSizePolicy.Policy) -> Self: ...

    @method(ClearRender)
    def update_view(self) -> void: ...

    @abstractmethod
    def render_view(self) -> Layout: ...
