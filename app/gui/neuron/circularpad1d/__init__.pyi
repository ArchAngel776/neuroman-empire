from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.circularpad1d.params import CircularPad1dParams
from app.network.neuron.circularpad1d.options import CircularPad1dOptions
from app.network.neuron.circularpad1d.boundary.params import CircularPad1dBoundaryParams
from app.network.neuron.circularpad1d.boundary.options import CircularPad1dBoundaryOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Boundary1dSwitcher, Boundary1dView


# Main

class NeuronBuilderCircularPadding1dStrategy(NeuronStrategy[CircularPad1dParams, CircularPad1dOptions]):
    class Watch(str):
        BOUNDARY_SWITCHER = ... #type: NeuronBuilderCircularPadding1dStrategy.Watch

    _bounded: FormInput[bool]

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[CircularPad1dParams, CircularPad1dOptions]: ...

    @property
    def default_params(self) -> CircularPad1dParams: ...

    @property
    def default_options(self) -> CircularPad1dOptions: ...

    def load(self, params: CircularPad1dParams, options: CircularPad1dOptions) -> void: ...

    @property
    def boundary_params(self) -> NeuronStrategyParams[CircularPad1dBoundaryParams, CircularPad1dBoundaryOptions]: ...

    @staticmethod
    def value_to_boundary(value: bool) -> Boundary1dView: ...

    def change_boundary(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def boundary_switcher_program(self) -> Boundary1dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
