from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.zeropad2d.params import ZeroPad2dParams
from app.network.neuron.zeropad2d.options import ZeroPad2dOptions
from app.network.neuron.zeropad2d.boundary.params import ZeroPad2dBoundaryParams
from app.network.neuron.zeropad2d.boundary.options import ZeroPad2dBoundaryOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Boundary2dSwitcher, Boundary2dView


# Main

class NeuronBuilderZeroPadding2dStrategy(NeuronStrategy[ZeroPad2dParams, ZeroPad2dOptions]):
    class Watch(str):
        BOUNDARY_SWITCHER = ... #type: NeuronBuilderZeroPadding2dStrategy.Watch

    _bounded: FormInput[bool]

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ZeroPad2dParams, ZeroPad2dOptions]: ...

    @property
    def default_params(self) -> ZeroPad2dParams: ...

    @property
    def default_options(self) -> ZeroPad2dOptions: ...

    def load(self, params: ZeroPad2dParams, options: ZeroPad2dOptions) -> void: ...

    @property
    def boundary_params(self) -> NeuronStrategyParams[ZeroPad2dBoundaryParams, ZeroPad2dBoundaryOptions]: ...

    @staticmethod
    def value_to_boundary(value: bool) -> Boundary2dView: ...

    def change_boundary(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def boundary_switcher_program(self) -> Boundary2dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...