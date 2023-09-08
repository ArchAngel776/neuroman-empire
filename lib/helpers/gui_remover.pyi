from typing import Union, TypeVar

from PyQt5.QtWidgets import QLayout, QWidget, QWidgetItem, QLayoutItem

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator

# Types

TGUIRemover = TypeVar("TGUIRemover", bound=GUIRemover)


# Decorators

class WidgetWithLayout(Decorator[void, [GUIRemover, QWidget]]):
    def method(self, target: TGUIRemover, widget: QWidget) -> void: ...


# Main

class GUIRemover:
    def remove_layout(self, layout: QLayout) -> void: ...

    @method(WidgetWithLayout)
    def remove_widget(self, widget: QWidget) -> void: ...

    def remove_item(self, item: Union[QLayoutItem, QWidgetItem]) -> void: ...

    def remove_item_layout(self, item: QLayout) -> void: ...

    def remove_item_widget(self, item: QWidget) -> void:  ...
