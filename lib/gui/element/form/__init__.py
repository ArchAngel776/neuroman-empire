from abc import ABC, abstractmethod

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element import Element


# Decorators

class UpdateControl(Decorator):
    def method(self, target, value, update_control=True):
        super().method(target, value)
        if target.form_control and update_control:
            target.sync()


class ExistsInput(Decorator):
    def method(self, target, value):
        if target.has_form_input():
            super().method(target, value)


# Meta

class FormControlMeta(type(Element), type(ABC)):
    pass


# Data

class FormInput:
    def __init__(self, value):
        self._value = value
        self._form_control = None

    def bind(self, form_control):
        self._form_control = form_control
        return self

    def sync(self):
        self.form_control.react(self.value)

    @method(UpdateControl)
    def update(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @property
    def form_control(self):
        return self._form_control


# Main

class FormControl(Element, ABC, metaclass=FormControlMeta):
    def __init__(self, root):
        super().__init__(root)
        self._form_input = None

    def Bind(self, form_input):
        self._form_input = form_input.bind(self)
        return self

    @abstractmethod
    def react(self, value):
        pass

    @method(ExistsInput)
    def input(self, value):
        self._form_input.update(value, False)

    def has_form_input(self):
        return self._form_input is not None

    @property
    def value(self):
        if not self.has_form_input():
            raise KeyError("Control hasn't been bound to any input.")
        return self._form_input.value
