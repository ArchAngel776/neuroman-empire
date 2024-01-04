from abc import ABC, abstractmethod

from lib.decorators.decorator import Decorator


# Decorators

class ValidationMethod(Decorator):
    def method(self, target, value):
        if value is None:
            return True
        elif callable(value):
            return super().method(target, value())
        else:
            return super().method(target, value)


# Main

class Validation(ABC):
    def __init__(self, data):
        self._data = data

    @abstractmethod
    def validate(self, target):
        pass

    @property
    def data(self):
        return self._data

    @property
    def error(self):
        return self.data["message"]
