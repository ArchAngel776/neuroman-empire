from typing import Callable, TypeVar

from PyQt5.QtGui import QCursor

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.component.switcher.strategy import SwitcherStrategy
from lib.gui.element.form.container import FormContainer
from lib.gui.layout import Layout

from app.network.neuron import Neuron
from app.gui import MainWindow
from app.gui.event.select_network import SelectNeuronEvent
from app.gui.neuron import NeuronBuilderSwitcher
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.network import NeuronOperationParams
from app.gui.network.dependencies import NeuronOperationDependencies

from .params import NeuronCreationParams

# Types

TNeuronOperationCreationStrategyCloseForm = TypeVar(
    "TNeuronOperationCreationStrategyCloseForm",
    bound=NeuronOperationCreationStrategy
)


# Decorators

class CloseForm(Decorator[bool, [NeuronOperationCreationStrategy]]):
    def method(self, target: TNeuronOperationCreationStrategyCloseForm) -> bool: ...


# Main

class NeuronOperationCreationStrategy(SwitcherStrategy[NeuronOperationDependencies, NeuronOperationParams]):
    class Watch(str):
        NEURON_SWITCHER_ELEMENT = ... #type: NeuronOperationCreationStrategy.Watch

    class NeuronGroup(str):
        CONV = ... #type: NeuronOperationCreationStrategy.NeuronGroup
        POOL = ... #type: NeuronOperationCreationStrategy.NeuronGroup
        LIN = ... #type: NeuronOperationCreationStrategy.NeuronGroup

    _neuron_name: FormInput[str]
    _neuron_type: FormInput[tuple[int, type[Neuron]]]

    _form_container: FormContainer

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

    @property
    def action_entry(self) -> Callable[[], void]: ...

    def validate_form(self) -> bool: ...

    def create_neuron(self) -> bool: ...

    @method(CloseForm)
    def cancel(self) -> bool: ...

    @property
    def switcher_program(self) -> NeuronBuilderSwitcher: ...

    @property
    def neuron_dependencies(self) -> NeuronBuilderDependencies: ...

    @property
    def form_container(self) -> FormContainer: ...

    def render(self, root: MainWindow) -> Layout: ...
