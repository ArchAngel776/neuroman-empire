from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.reflectionpad2d.params import ReflectionPad2dParams
from app.network.neuron.reflectionpad2d.options import ReflectionPad2dOptions
from app.network.neuron.reflectionpad2d.boundary.params import ReflectionPad2dBoundaryParams
from app.network.neuron.reflectionpad2d.boundary.options import ReflectionPad2dBoundaryOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Boundary2dSwitcher, Boundary2dView


# Main

class NeuronBuilderReflectionPadding2dStrategy(NeuronStrategy[ReflectionPad2dParams, ReflectionPad2dOptions]):
    class Watch(str):
        BOUNDARY_SWITCHER = ... #type: NeuronBuilderReflectionPadding2dStrategy.Watch

    _bounded: FormInput[bool]

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ReflectionPad2dParams, ReflectionPad2dOptions]: ...

    @property
    def default_params(self) -> ReflectionPad2dParams: ...

    @property
    def default_options(self) -> ReflectionPad2dOptions: ...

    def load(self, params: ReflectionPad2dParams, options: ReflectionPad2dOptions) -> void: ...

    @property
    def boundary_params(self) -> NeuronStrategyParams[ReflectionPad2dBoundaryParams, ReflectionPad2dBoundaryOptions]: ...

    @staticmethod
    def value_to_boundary(value: bool) -> Boundary2dView: ...

    def change_boundary(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def boundary_switcher_program(self) -> Boundary2dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
