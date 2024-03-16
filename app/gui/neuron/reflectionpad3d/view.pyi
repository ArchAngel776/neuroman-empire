from enum import Enum

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.neuron.reflectionpad3d.boundary.params import ReflectionPad3dBoundaryParams
from app.network.neuron.reflectionpad3d.boundary.options import ReflectionPad3dBoundaryOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.extension.reflectionpad.bounded import BoundedBoundaryStrategy
from app.gui.neuron.reflectionpad3d.boundary import UnboundedBoundaryStrategy


# View

class Boundary3dView(Enum):
    BOUNDED = ... #type: Boundary3dView
    UNBOUNDED = ... #type: Boundary3dView


# Main

class Boundary3dSwitcher(
    SwitcherProgram[
        Boundary3dView,
        NeuronBuilderDependencies,
        NeuronStrategyParams[ReflectionPad3dBoundaryParams, ReflectionPad3dBoundaryOptions]
    ]
):
    _bounded_strategy: BoundedBoundaryStrategy
    _unbounded_strategy: UnboundedBoundaryStrategy

    def __init__(self, key: Boundary3dView, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Boundary3dView, NeuronStrategy[ReflectionPad3dBoundaryParams, ReflectionPad3dBoundaryOptions]
    ]: ...

    @property
    def current_strategy(self) -> NeuronStrategy[ReflectionPad3dBoundaryParams, ReflectionPad3dBoundaryOptions]: ...
