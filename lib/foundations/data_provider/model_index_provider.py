from PyQt5.QtCore import QModelIndex

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.foundations.data_provider import DataProvider


# Decorators

class SingleIndexValidation(Decorator):
    def config(self, target, *data):
        if not len(data) == 1:
            raise ValueError("Only single index provision is allowed.")
        return self


# Main

class ModelIndexProvider(DataProvider):
    def __init__(self):
        self._index = QModelIndex()

    @method(SingleIndexValidation)
    def add(self, *data):
        self._index = data[0]

    def provide(self):
        return self._index

    def clear(self):
        self._index = QModelIndex()
