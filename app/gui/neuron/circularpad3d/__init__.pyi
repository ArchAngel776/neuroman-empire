from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.circularpad3d.params import CircularPad3dParams
from app.network.neuron.circularpad3d.options import CircularPad3dOptions
from app.network.neuron.circularpad3d.boundary.params import CircularPad3dBoundaryParams
from app.network.neuron.circularpad3d.boundary.options import CircularPad3dBoundaryOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Boundary3dSwitcher, Boundary3dView


# Main

class NeuronBuilderCircularPadding3dStrategy(NeuronStrategy[CircularPad3dParams, CircularPad3dOptions]):
    class Watch(str):
        BOUNDARY_SWITCHER = ... #type: NeuronBuilderCircularPadding3dStrategy.Watch

    _bounded: FormInput[bool]

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[CircularPad3dParams, CircularPad3dOptions]: ...

    @property
    def default_params(self) -> CircularPad3dParams: ...

    @property
    def default_options(self) -> CircularPad3dOptions: ...

    def load(self, params: CircularPad3dParams, options: CircularPad3dOptions) -> void: ...

    @property
    def boundary_params(self) -> NeuronStrategyParams[CircularPad3dBoundaryParams, CircularPad3dBoundaryOptions]: ...

    @staticmethod
    def value_to_boundary(value: bool) -> Boundary3dView: ...

    def change_boundary(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def boundary_switcher_program(self) -> Boundary3dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
