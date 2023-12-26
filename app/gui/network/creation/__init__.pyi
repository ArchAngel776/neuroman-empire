from typing import Callable

from PyQt5.QtGui import QCursor

from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.switcher.strategy import SwitcherStrategy
from lib.gui.layout import Layout

from app.network.neuron import Neuron
from app.gui import MainWindow
from app.gui.event.select_network import SelectNeuronEvent
from app.gui.neuron import NeuronBuilderSwitcher
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.network import NeuronOperationParams
from app.gui.network.dependencies import NeuronOperationDependencies

from .params import NeuronCreationParams


# Main

class NeuronOperationCreationStrategy(SwitcherStrategy[NeuronOperationDependencies, NeuronOperationParams]):
    NEURON_SWITCHER_ELEMENT = ... #type: str

    _neuron_name: FormInput[str]
    _neuron_type: FormInput[tuple[int, type[Neuron]]]

    _form_title_font: Font
    _form_label_font: Font

    _button_cursor: QCursor

    def __init__(self, dependencies: NeuronOperationDependencies) -> None: ...

    @property
    def params(self) -> NeuronCreationParams: ...

    def select_neuron(self, event: SelectNeuronEvent) -> bool: ...

    @property
    def neuron_index(self) -> int: ...

    @property
    def neuron_type(self) -> type[Neuron]: ...

    @property
    def create(self) -> Callable[[type[Neuron]], void]: ...

    def create_neuron(self) -> bool: ...

    @property
    def switcher_program(self) -> NeuronBuilderSwitcher: ...

    @property
    def neuron_dependencies(self) -> NeuronBuilderDependencies: ...

    def render(self, root: MainWindow) -> Layout: ...
