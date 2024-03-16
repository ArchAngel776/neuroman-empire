from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.reflectionpad3d.params import ReflectionPad3dParams
from app.network.neuron.reflectionpad3d.options import ReflectionPad3dOptions
from app.network.neuron.reflectionpad3d.boundary.params import ReflectionPad3dBoundaryParams
from app.network.neuron.reflectionpad3d.boundary.options import ReflectionPad3dBoundaryOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Boundary3dSwitcher, Boundary3dView


# Main

class NeuronBuilderReflectionPadding3dStrategy(NeuronStrategy[ReflectionPad3dParams, ReflectionPad3dOptions]):
    class Watch(str):
        BOUNDARY_SWITCHER = ... #type: NeuronBuilderReflectionPadding3dStrategy.Watch

    _bounded: FormInput[bool]

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ReflectionPad3dParams, ReflectionPad3dOptions]: ...

    @property
    def default_params(self) -> ReflectionPad3dParams: ...

    @property
    def default_options(self) -> ReflectionPad3dOptions: ...

    def load(self, params: ReflectionPad3dParams, options: ReflectionPad3dOptions) -> void: ...

    @property
    def boundary_params(self) -> NeuronStrategyParams[ReflectionPad3dBoundaryParams, ReflectionPad3dBoundaryOptions]: ...

    @staticmethod
    def value_to_boundary(value: bool) -> Boundary3dView: ...

    def change_boundary(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def boundary_switcher_program(self) -> Boundary3dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
