from typing import Callable, TypeVar

from PyQt5.QtWidgets import QMenuBar, QMenu, QAction

from lib.decorators import method
from lib.decorators.decorator import Decorator

# Types

TMenu = TypeVar("TMenu", bound=Menu)
TMenuConnect = TypeVar("TMenuConnect", bound=Menu)


# Decorators

class ConnectAction(Decorator[Menu, [Menu, str, QAction, Callable]]):
    def method(self, target: TMenuConnect, name: str, action: QAction, callback: Callable) -> TMenuConnect: ...


# Main

class Menu:
    _menu: QMenuBar
    _actions: dict[str, QMenu]

    def __init__(self, menu: QMenuBar) -> None: ...

    def create(self: TMenu, name: str, title: str) -> TMenu: ...

    @method(ConnectAction)
    def add(self: TMenu, name: str, action: QAction) -> TMenu: ...

    def get(self, name: str) -> QMenu: ...
