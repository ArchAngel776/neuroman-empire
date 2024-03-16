from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.circularpad2d.params import CircularPad2dParams
from app.network.neuron.circularpad2d.options import CircularPad2dOptions
from app.network.neuron.circularpad2d.boundary.params import CircularPad2dBoundaryParams
from app.network.neuron.circularpad2d.boundary.options import CircularPad2dBoundaryOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Boundary2dSwitcher, Boundary2dView


# Main

class NeuronBuilderCircularPadding2dStrategy(NeuronStrategy[CircularPad2dParams, CircularPad2dOptions]):
    class Watch(str):
        BOUNDARY_SWITCHER = ... #type: NeuronBuilderCircularPadding2dStrategy.Watch

    _bounded: FormInput[bool]

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[CircularPad2dParams, CircularPad2dOptions]: ...

    @property
    def default_params(self) -> CircularPad2dParams: ...

    @property
    def default_options(self) -> CircularPad2dOptions: ...

    def load(self, params: CircularPad2dParams, options: CircularPad2dOptions) -> void: ...

    @property
    def boundary_params(self) -> NeuronStrategyParams[CircularPad2dBoundaryParams, CircularPad2dBoundaryOptions]: ...

    @staticmethod
    def value_to_boundary(value: bool) -> Boundary2dView: ...

    def change_boundary(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def boundary_switcher_program(self) -> Boundary2dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
