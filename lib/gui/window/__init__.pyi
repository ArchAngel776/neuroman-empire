from typing import TypeVar, Self

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.screen import Screen

from .sizer import Sizer

# Types

TWindowConfig = TypeVar("TWindowConfig", bound=Window)


# Decorators

class ConfigScreen(Decorator[void, [Window, Screen[Window]]]):
    def config(self, target: TWindowConfig, screen: Screen[TWindowConfig]) -> Self: ...


# Main

class Window(QWidget):
    _title: str
    _icon: QIcon
    _sizer: Sizer

    def __init__(self, title: str, icon: QIcon, sizer: Sizer) -> None: ...

    def config(self) -> void: ...

    @method(ConfigScreen)
    def display(self, screen: Screen[Self]) -> void: ...
