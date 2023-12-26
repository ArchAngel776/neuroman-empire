from typing import Callable

from PyQt5.QtGui import QCursor

from lib import void
from lib.gui.element.font import Font
from lib.gui.element.switcher import Switcher
from lib.gui.element.switcher.strategy import SwitcherStrategy
from lib.gui.layout import Layout

from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.gui import MainWindow
from app.gui.neuron import NeuronParams, NeuronBuilderSwitcher
from app.gui.neuron.dependencies import NeuronBuilderDependencies
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

    @property
    def remove(self) -> Callable[[Neuron], void]: ...

    @property
    def action_entry(self) -> Callable[[], void]: ...

    def modify_neuron(self) -> bool: ...

    def remove_neuron(self) -> bool: ...

    def cancel(self) -> bool: ...

    @staticmethod
    def init_switcher(switcher: Switcher[NeuronType, {}, NeuronParams]) -> bool: ...

    @property
    def switcher_program(self) -> NeuronBuilderSwitcher: ...

    @property
    def neuron_dependencies(self) -> NeuronBuilderDependencies: ...

    def render(self, root: MainWindow) -> Layout: ...
