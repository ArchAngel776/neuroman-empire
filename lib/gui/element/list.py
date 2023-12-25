from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLayout, QSizePolicy

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.layout.type import LayoutType
from lib.helpers.gui_remover import GUIRemover
from lib.hooks import entities, layout_widget
from lib.gui.element import Element
from lib.gui.layout.factory import LayoutFactory


# Decorators


class ClearLayout(Decorator):
    def __init__(self, original):
        super().__init__(original)
        self._gui_remover = GUIRemover()

    def config(self, target):
        self._gui_remover.remove_widget(target)
        return self


# Main

class List(Element):
    def __init__(self, root, source_getter, orientation):
        super().__init__(root)
        self._source_getter = source_getter
        self._orientation = orientation
        self._callback_builder = None
        self._sizing = QSizePolicy()

    def config(self):
        super().config()

        if self._orientation == LayoutType.HORIZONTAL:
            self.setLayout(QHBoxLayout())
        elif self._orientation == LayoutType.VERTICAL:
            self.setLayout(QVBoxLayout())

        self.update_list()

    def InnerSizing(self, horizontal, vertical):
        self._sizing.setHorizontalPolicy(horizontal)
        self._sizing.setVerticalPolicy(vertical)
        return self

    def Render(self, callback_builder):
        self._callback_builder = callback_builder
        return self

    @method(ClearLayout)
    def update_list(self):
        layout = LayoutFactory(self._orientation).create()
        for index, item in entities(self._source_getter()):
            layout.append(self.callback_builder(item, index))

        widget = layout_widget(layout.element)
        widget.setSizePolicy(self._sizing)

        self.layout().addWidget(widget)

    @property
    def callback_builder(self):
        if not self._callback_builder:
            raise AttributeError("Callback builder hasn't been provided yet.")
        return self._callback_builder
