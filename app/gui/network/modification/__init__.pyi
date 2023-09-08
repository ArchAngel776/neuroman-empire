from PyQt5.QtGui import QCursor

from lib.gui.element.font import Font
from lib.gui.element.switcher import Switcher
from lib.gui.element.switcher.strategy import SwitcherStrategy
from lib.gui.layout import Layout

from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.gui import MainWindow
from app.gui.neuron import NeuronParams, NeuronBuilderSwitcher, NeuronDependencies
from app.gui.network.dependencies import NeuronOperationDependencies
from app.gui.network import NeuronOperationParams


# Main

class NeuronOperationModificationStrategy(SwitcherStrategy[NeuronOperationDependencies, NeuronOperationParams]):
    NEURON_SWITCHER_ELEMENT = ... #type: str

    _form_title_font: Font
    _form_label_font: Font
    _form_value_font: Font

    _button_cursor: QCursor

    def __init__(self, dependencies: NeuronOperationDependencies) -> None: ...

    def params(self) -> NeuronOperationParams: ...

    @property
    def neuron(self) -> Neuron: ...

    @property
    def neuron_type(self) -> NeuronType: ...

    @staticmethod
    def init_switcher(switcher: Switcher[NeuronType, {}, NeuronParams]) -> bool: ...

    def modify_neuron(self) -> bool: ...

    def cancel(self) -> bool: ...

    @property
    def switcher_program(self) -> NeuronBuilderSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
