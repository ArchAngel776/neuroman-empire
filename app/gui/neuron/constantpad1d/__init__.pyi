from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.constantpad1d.params import ConstantPad1dParams
from app.network.neuron.constantpad1d.options import ConstantPad1dOptions
from app.network.neuron.constantpad1d.boundary.params import ConstantPad1dBoundaryParams
from app.network.neuron.constantpad1d.boundary.options import ConstantPad1dBoundaryOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Boundary1dSwitcher, Boundary1dView


# Main

class NeuronBuilderConstantPadding1dStrategy(NeuronStrategy[ConstantPad1dParams, ConstantPad1dOptions]):
    class Watch(str):
        BOUNDARY_SWITCHER = ... #type: NeuronBuilderConstantPadding1dStrategy.Watch

    _value: FormInput[float]

    _bounded: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ConstantPad1dParams, ConstantPad1dOptions]: ...

    @property
    def default_params(self) -> ConstantPad1dParams: ...

    @property
    def default_options(self) -> ConstantPad1dOptions: ...

    def load(self, params: ConstantPad1dParams, options: ConstantPad1dOptions) -> void: ...

    @property
    def boundary_params(self) -> NeuronStrategyParams[ConstantPad1dBoundaryParams, ConstantPad1dBoundaryOptions]: ...

    @staticmethod
    def value_to_boundary(value: bool) -> Boundary1dView: ...

    def change_boundary(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def boundary_switcher_program(self) -> Boundary1dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
