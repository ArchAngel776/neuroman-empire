from PyQt5.QtCore import QObject, pyqtSignal

from lib.decorators import method
from lib.decorators.decorator import Decorator


# Decorators

class ConfigElement(Decorator):
    def config(self, target, element):
        element.config()
        return self


class ConnectClose(Decorator):
    def config(self, target, element):
        target.closed.connect(element.close_exception)
        return self


class NoRepeatUpdate(Decorator):
    def method(self, target, is_valid):
        if target.is_valid:
            super().method(target, is_valid)


# Main

class FormContainer(QObject):
    closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._elements = []
        self._is_valid = True

    @method(ConfigElement)
    @method(ConnectClose)
    def add(self, element):
        self._elements.append(element)
        return self

    def validate(self):
        self._is_valid = True
        for element in self._elements:
            element.validate()

    def close(self):
        self.closed.emit()

    # Slots

    @method(NoRepeatUpdate)
    def update_validation_status(self, is_valid):
        self._is_valid = is_valid

    def remove_element(self, element):
        self._elements.remove(element)

    @property
    def is_valid(self):
        return self._is_valid
