from abc import ABC, abstractmethod

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QSizePolicy

from lib.hooks import layout_widget
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.helpers.gui_remover import GUIRemover
from lib.gui import Watcher
from lib.gui.element import Element
from lib.gui.layout.type import LayoutType


# Decorators

class ClearRender(Decorator):
    def __init__(self, original):
        super().__init__(original)
        self._remover = GUIRemover()

    def config(self, target):
        self._remover.remove_widget(target)
        return self


# Meta

class ComponentMeta(type(Element), type(ABC)):
    pass


# Main

class Component(Element, Watcher, ABC, metaclass=ComponentMeta):
    def __init__(self, root, orientation):
        super().__init__(root)
        self._orientation = orientation
        self._sizing = QSizePolicy()

    def config(self):
        super().config()
        match self._orientation:
            case LayoutType.HORIZONTAL:
                self.setLayout(QHBoxLayout())
            case LayoutType.VERTICAL:
                self.setLayout(QVBoxLayout())
            case _:
                raise ValueError("Cannot handle specified layout type.")

    def InnerSizing(self, horizontal, vertical):
        self._sizing.setHorizontalPolicy(horizontal)
        self._sizing.setVerticalPolicy(vertical)
        return self

    @method(ClearRender)
    def update_view(self):
        widget = layout_widget(self.render_view(self.root).element)
        widget.setSizePolicy(self._sizing)

        self.layout().addWidget(widget)

    @abstractmethod
    def render_view(self, root):
        pass
