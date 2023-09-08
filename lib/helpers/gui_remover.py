from PyQt5.QtWidgets import QLayout, QWidgetItem

from lib.decorators import method
from lib.decorators.decorator import Decorator


# Decorators

class WidgetWithLayout(Decorator):
    def method(self, target, widget):
        if widget.layout():
            super().method(target, widget)


# Main

class GUIRemover:
    def remove_layout(self, layout):
        for index in range(layout.count()):
            self.remove_item(layout.itemAt(index))

    @method(WidgetWithLayout)
    def remove_widget(self, widget):
        for index in range(widget.layout().count()):
            self.remove_item(widget.layout().itemAt(index))

    def remove_item(self, item):
        if isinstance(item, QLayout):
            self.remove_item_layout(item)
        elif isinstance(item, QWidgetItem):
            self.remove_item_widget(item.widget())

    def remove_item_layout(self, item):
        self.remove_layout(item)
        item.deleteLater()

    def remove_item_widget(self, item):
        self.remove_widget(item)
        item.deleteLater()
