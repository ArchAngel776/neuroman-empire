from PyQt5.QtCore import QModelIndex


# Main

class Counter:
    def __init__(self):
        self._position = 0
        self._index = QModelIndex()

    def increment_position(self):
        self._position += 1

    def setup(self, index):
        self._index = index
        return self

    @property
    def position(self):
        return self._position

    @property
    def index(self):
        return self._index
