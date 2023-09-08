from PyQt5.QtCore import QSize


# Main

class Sizer:
    def __init__(self, min_width, min_height, max_width, max_height):
        self._min = QSize(min_width, min_height)
        self._max = QSize(max_width, max_height)

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max
