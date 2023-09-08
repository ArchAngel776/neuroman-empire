from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element import Element


# Decorators

class ExistsInput(Decorator):
    def method(self, target, value):
        if target.has_form_input():
            super().method(target, value)


# Data

class FormInput:
    def __init__(self, value):
        self._value = value

    def update(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


# Main

class FormControl(Element):
    def __init__(self, root):
        super().__init__(root)
        self._form_input = None

    def Bind(self, form_input):
        self._form_input = form_input
        return self

    @method(ExistsInput)
    def input(self, value):
        self._form_input.update(value)

    def has_form_input(self):
        return self._form_input is not None
