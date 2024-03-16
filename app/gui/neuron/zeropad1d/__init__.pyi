from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.zeropad1d.params import ZeroPad1dParams
from app.network.neuron.zeropad1d.options import ZeroPad1dOptions
from app.network.neuron.zeropad1d.boundary.params import ZeroPad1dBoundaryParams
from app.network.neuron.zeropad1d.boundary.options import ZeroPad1dBoundaryOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Boundary1dSwitcher, Boundary1dView


# Main

class NeuronBuilderZeroPadding1dStrategy(NeuronStrategy[ZeroPad1dParams, ZeroPad1dOptions]):
    class Watch(str):
        BOUNDARY_SWITCHER = ... #type: NeuronBuilderZeroPadding1dStrategy.Watch

    _bounded: FormInput[bool]

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ZeroPad1dParams, ZeroPad1dOptions]: ...

    @property
    def default_params(self) -> ZeroPad1dParams: ...

    @property
    def default_options(self) -> ZeroPad1dOptions: ...

    def load(self, params: ZeroPad1dParams, options: ZeroPad1dOptions) -> void: ...

    @property
    def boundary_params(self) -> NeuronStrategyParams[ZeroPad1dBoundaryParams, ZeroPad1dBoundaryOptions]: ...

    @staticmethod
    def value_to_boundary(value: bool) -> Boundary1dView: ...

    def change_boundary(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def boundary_switcher_program(self) -> Boundary1dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
