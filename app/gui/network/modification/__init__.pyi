from typing import Callable

from PyQt5.QtGui import QCursor

from app.gui.neuron.params import NeuronStrategyParams
from lib import void
from lib.gui.element.font import Font
from lib.gui.element.component.switcher.strategy import SwitcherStrategy
from lib.gui.layout import Layout

from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.gui import MainWindow
from app.gui.neuron import NeuronBuilderSwitcher, NeuronParams, NeuronOptions
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.network.dependencies import NeuronOperationDependencies
from app.gui.network import NeuronOperationParams


# Main

class NeuronOperationModificationStrategy(SwitcherStrategy[NeuronOperationDependencies, NeuronOperationParams]):
    class Watch(str):
        NEURON_SWITCHER_ELEMENT = ... #type: NeuronOperationModificationStrategy.Watch

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

    def init_switcher(
            self,
            neuron_strategy: SwitcherStrategy[
                NeuronBuilderDependencies, NeuronStrategyParams[NeuronParams, NeuronOptions]
            ]
    ) -> void: ...

    @property
    def switcher_program(self) -> NeuronBuilderSwitcher: ...

    @property
    def neuron_dependencies(self) -> NeuronBuilderDependencies: ...

    def render(self, root: MainWindow) -> Layout: ...
