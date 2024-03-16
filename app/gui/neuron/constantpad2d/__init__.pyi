from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.constantpad2d.params import ConstantPad2dParams
from app.network.neuron.constantpad2d.options import ConstantPad2dOptions
from app.network.neuron.constantpad2d.boundary.params import ConstantPad2dBoundaryParams
from app.network.neuron.constantpad2d.boundary.options import ConstantPad2dBoundaryOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Boundary2dSwitcher, Boundary2dView


# Main

class NeuronBuilderConstantPadding2dStrategy(NeuronStrategy[ConstantPad2dParams, ConstantPad2dOptions]):
    class Watch(str):
        BOUNDARY_SWITCHER = ... #type: NeuronBuilderConstantPadding2dStrategy.Watch

    _value: FormInput[float]

    _bounded: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ConstantPad2dParams, ConstantPad2dOptions]: ...

    @property
    def default_params(self) -> ConstantPad2dParams: ...

    @property
    def default_options(self) -> ConstantPad2dOptions: ...

    def load(self, params: ConstantPad2dParams, options: ConstantPad2dOptions) -> void: ...

    @property
    def boundary_params(self) -> NeuronStrategyParams[ConstantPad2dBoundaryParams, ConstantPad2dBoundaryOptions]: ...

    @staticmethod
    def value_to_boundary(value: bool) -> Boundary2dView: ...

    def change_boundary(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def boundary_switcher_program(self) -> Boundary2dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
