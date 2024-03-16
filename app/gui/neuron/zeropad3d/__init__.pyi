from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.zeropad3d.params import ZeroPad3dParams
from app.network.neuron.zeropad3d.options import ZeroPad3dOptions
from app.network.neuron.zeropad3d.boundary.params import ZeroPad3dBoundaryParams
from app.network.neuron.zeropad3d.boundary.options import ZeroPad3dBoundaryOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Boundary3dSwitcher, Boundary3dView


# Main

class NeuronBuilderZeroPadding3dStrategy(NeuronStrategy[ZeroPad3dParams, ZeroPad3dOptions]):
    class Watch(str):
        BOUNDARY_SWITCHER = ... #type: NeuronBuilderZeroPadding3dStrategy.Watch

    _bounded: FormInput[bool]

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ZeroPad3dParams, ZeroPad3dOptions]: ...

    @property
    def default_params(self) -> ZeroPad3dParams: ...

    @property
    def default_options(self) -> ZeroPad3dOptions: ...

    def load(self, params: ZeroPad3dParams, options: ZeroPad3dOptions) -> void: ...

    @property
    def boundary_params(self) -> NeuronStrategyParams[ZeroPad3dBoundaryParams, ZeroPad3dBoundaryOptions]: ...

    @staticmethod
    def value_to_boundary(value: bool) -> Boundary3dView: ...

    def change_boundary(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def boundary_switcher_program(self) -> Boundary3dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
