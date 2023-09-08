from lib.decorators import method
from lib.decorators.decorator import Decorator


# Decorators

class ConfigElement(Decorator):
    def config(self, target, element):
        element.config()
        return self


# Main

class Layout:
    def __init__(self, layout):
        self._layout = layout
        self._weight = 1

    def weight(self, weight):
        self._weight = weight
        return self

    @method(ConfigElement)
    def add(self, element):
        self._layout.addWidget(element)
        return self

    def append(self, layout):
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
