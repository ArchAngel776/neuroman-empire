from PyQt5.QtGui import QCursor

from lib.gui.element.font import Font
from lib.gui.layout import Layout
from lib.gui.screen import Screen

from app.gui import MainWindow


# Main

class HomeScreen(Screen[MainWindow]):
    _title_font: Font
    _caption_font: Font

    _button_cursor: QCursor

    def __init__(self, root: MainWindow) -> None: ...

    def create_new_network(self) -> bool: ...

    def render(self) -> Layout: ...
