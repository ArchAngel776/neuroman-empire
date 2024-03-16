from enum import Enum

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.neuron.reflectionpad2d.boundary.params import ReflectionPad2dBoundaryParams
from app.network.neuron.reflectionpad2d.boundary.options import ReflectionPad2dBoundaryOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.extension.reflectionpad.bounded import BoundedBoundaryStrategy
from app.gui.neuron.reflectionpad2d.boundary import UnboundedBoundaryStrategy


# View

class Boundary2dView(Enum):
    BOUNDED = ... #type: Boundary2dView
    UNBOUNDED = ... #type: Boundary2dView


# Main

class Boundary2dSwitcher(
    SwitcherProgram[
        Boundary2dView,
        NeuronBuilderDependencies,
        NeuronStrategyParams[ReflectionPad2dBoundaryParams, ReflectionPad2dBoundaryOptions]
    ]
):
    _bounded_strategy: BoundedBoundaryStrategy
    _unbounded_strategy: UnboundedBoundaryStrategy

    def __init__(self, key: Boundary2dView, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Boundary2dView, NeuronStrategy[ReflectionPad2dBoundaryParams, ReflectionPad2dBoundaryOptions]
    ]: ...

    @property
    def current_strategy(self) -> NeuronStrategy[ReflectionPad2dBoundaryParams, ReflectionPad2dBoundaryOptions]: ...
