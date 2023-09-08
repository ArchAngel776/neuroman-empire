from PyQt5.QtWidgets import QWidget

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.window.sizer import Sizer


# Decorators

class ConfigScreen(Decorator):
    def config(self, target, screen):
        screen.config()
        return self


# Main

class Window(QWidget):
    def __init__(self, title, icon, sizer):
        super().__init__()
        self._title = title
        self._icon = icon
        self._sizer = sizer

    def config(self):
        self.setWindowTitle(self._title)
        self.setWindowIcon(self._icon)

        self.setMinimumSize(self._sizer.min)
        self.setMaximumSize(self._sizer.max)

    @method(ConfigScreen)
    def display(self, screen):
        self.setLayout(screen.render().element)
