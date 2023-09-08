from typing import TypeVar

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.screen import Screen

from .sizer import Sizer

# Types

TWindow = TypeVar("TWindow", bound=Window)
TWindowConfig = TypeVar("TWindowConfig", bound=Window)


# Decorators

class ConfigScreen(Decorator[void, [Window, Screen[Window]]]):
    def config(self, target: TWindowConfig, screen: Screen[TWindowConfig]) -> ConfigScreen: ...


# Main

class Window(QWidget):
    _title: str
    _icon: QIcon
    _sizer: Sizer

    def __init__(self, title: str, icon: QIcon, sizer: Sizer) -> None: ...

    def config(self) -> void: ...

    @method(ConfigScreen)
    def display(self: TWindow, screen: Screen[TWindow]) -> void: ...
