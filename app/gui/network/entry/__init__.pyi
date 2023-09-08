from PyQt5.QtGui import QCursor

from lib.gui.element.font import Font
from lib.gui.element.switcher.strategy import SwitcherStrategy
from lib.gui.layout import Layout

from app.gui import MainWindow
from app.gui.network.dependencies import NeuronOperationDependencies

from .params import NeuronEntryParams


# Main

class NeuronOperationEntryStrategy(SwitcherStrategy[NeuronOperationDependencies, NeuronEntryParams]):
    _form_title_font: Font
    _form_description_font: Font

    _button_cursor: QCursor

    def __init__(self, dependencies: NeuronOperationDependencies) -> None: ...

    @property
    def params(self) -> NeuronEntryParams: ...

    def action_creation(self) -> bool: ...

    def render(self, root: MainWindow) -> Layout: ...
