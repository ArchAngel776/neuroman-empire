from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.reflectionpad1d.params import ReflectionPad1dParams
from app.network.neuron.reflectionpad1d.options import ReflectionPad1dOptions
from app.network.neuron.reflectionpad1d.boundary.params import ReflectionPad1dBoundaryParams
from app.network.neuron.reflectionpad1d.boundary.options import ReflectionPad1dBoundaryOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Boundary1dSwitcher, Boundary1dView


# Main

class NeuronBuilderReflectionPadding1dStrategy(NeuronStrategy[ReflectionPad1dParams, ReflectionPad1dOptions]):
    class Watch(str):
        BOUNDARY_SWITCHER = ... #type: NeuronBuilderReflectionPadding1dStrategy.Watch

    _bounded: FormInput[bool]

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ReflectionPad1dParams, ReflectionPad1dOptions]: ...

    @property
    def default_params(self) -> ReflectionPad1dParams: ...

    @property
    def default_options(self) -> ReflectionPad1dOptions: ...

    def load(self, params: ReflectionPad1dParams, options: ReflectionPad1dOptions) -> void: ...

    @property
    def boundary_params(self) -> NeuronStrategyParams[ReflectionPad1dBoundaryParams, ReflectionPad1dBoundaryOptions]: ...

    @staticmethod
    def value_to_boundary(value: bool) -> Boundary1dView: ...

    def change_boundary(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def boundary_switcher_program(self) -> Boundary1dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
