from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.helpers.gui_remover import GUIRemover


# Decorators

class ConfigElement(Decorator):
    def config(self, target, element):
        element.config()
        return self


class ConditionalAdd(Decorator):
    def __init__(self, original):
        super().__init__(original)
        self._gui_remover = GUIRemover()

    def method(self, target, element, allow=True):
        if allow:
            return super().method(target, element)
        else:
            self._gui_remover.remove_widget(element)
            element.deleteLater()
            return target


class ConditionalAppend(Decorator):
    def __init__(self, original):
        super().__init__(original)
        self._gui_remover = GUIRemover()

    def method(self, target, *layouts, allow=True):
        if allow:
            return super().method(target, *layouts)
        else:
            for layout in layouts:
                self._gui_remover.remove_layout(layout.element)
                layout.element.deleteLater()
            return target


# Main

class Layout:
    def __init__(self, layout):
        self._layout = layout
        self._weight = 1

    def weight(self, weight):
        self._weight = weight
        return self

    @method(ConditionalAdd)
    @method(ConfigElement)
    def add(self, element):
        self._layout.addWidget(element)
        return self

    @method(ConditionalAppend)
    def append(self, *layouts):
        for layout in layouts:
            self._layout.addLayout(layout.element, layout.get_weight())
        return self

    def stretch(self):
        self._layout.addStretch()
        return self

    def constraint(self, constraint):
        self._layout.setSizeConstraint(constraint)
        return self

    def align(self, alignment):
        self._layout.setAlignment(alignment)
        return self

    def margin(self, horizontal, vertical):
        self._layout.setContentsMargins(horizontal, vertical, horizontal, vertical)
        return self

    def margin_horizontal(self, size):
        self.margin(size, 0)
        return self

    def margin_vertical(self, size):
        self.margin(0, size)
        return self

    @property
    def element(self):
        return self._layout

    def get_weight(self):
        return self._weight
