from pathlib import Path

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

from lib.decorators import method
from lib.gui.window import Window, ConfigScreen
from lib.gui.window.menu import Menu
from lib.gui.window.sizer import Sizer
from lib.hooks import layout_widget

from app import GUI_TITLE, GUI_SIZE_WIDTH, GUI_SIZE_HEIGHT
from app.hooks import main_icon, i18n
from app.gui.screen.home import HomeScreen
from app.gui.screen.network.create import CreateNetworkScreen


# Main

class MainWindow(QMainWindow, Window):
    MENU_HOME = "home"

    TAB_PROGRAM = i18n("window.menu.0.name")

    ACTION_HOME = i18n("window.menu.0.actions.home.name")
    ACTION_CLOSE = i18n("window.menu.0.actions.close.name")

    def __init__(self, title, icon, sizer):
        super().__init__(title, icon, sizer)
        self._menu = Menu(self.menuBar())

    def config(self):
        super().config()
        self.menu_init()

    def menu_init(self):
        self._menu.create(MainWindow.MENU_HOME, MainWindow.TAB_PROGRAM)

        self._menu.add(MainWindow.MENU_HOME, QAction(MainWindow.ACTION_HOME, self), self.home)
        self._menu.add(MainWindow.MENU_HOME, QAction(MainWindow.ACTION_CLOSE, self), self.close)

    @method(ConfigScreen)
    def display(self, screen):
        self.setCentralWidget(layout_widget(screen.render().element))

    def home(self):
        self.display(HomeScreen(self))

    def create_network(self, network):
        self.display(CreateNetworkScreen(self, network))


class GUI:
    def __init__(self, args):
        self._app = QApplication(args)
        self._main_window = MainWindow(
            title=GUI_TITLE,
            sizer=Sizer(GUI_SIZE_WIDTH, GUI_SIZE_HEIGHT, GUI_SIZE_WIDTH, GUI_SIZE_HEIGHT),
            icon=main_icon()
        )

    def config(self):
        self._app.setStyleSheet(Path("assets/style.qss").read_text())

    def start_gui_cycle(self):
        self._main_window.config()
        self._main_window.show()

        self._main_window.home()

        return self._app.exec_()
