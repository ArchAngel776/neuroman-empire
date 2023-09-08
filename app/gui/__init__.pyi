from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

from lib import void
from lib.decorators import method
from lib.gui.screen import Screen
from lib.gui.window import Window, ConfigScreen
from lib.gui.window.menu import Menu
from lib.gui.window.sizer import Sizer

from app.network import Network

from .screen.home import HomeScreen
from .screen.network.create import CreateNetworkScreen


# Main

class MainWindow(QMainWindow, Window):
    MENU_HOME = ... #type: str

    TAB_PROGRAM = ... #type: str

    ACTION_HOME = ... #type: str
    ACTION_CLOSE = ... #type: str

    _menu: Menu

    def __init__(self, title: str, icon: QIcon, sizer: Sizer) -> None: ...

    def config(self) -> void: ...

    def menu_init(self) -> void: ...

    @method(ConfigScreen)
    def display(self, screen: Screen) -> void: ...

    def home(self) -> void: ...

    def create_network(self, network: Network) -> void: ...


class GUI:
    _app: QApplication
    _main_window: MainWindow

    def __init__(self, args: list[str]) -> None: ...

    def config(self) -> void: ...

    def start_gui_cycle(self) -> int: ...
