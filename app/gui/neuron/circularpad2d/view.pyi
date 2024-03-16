from enum import Enum

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.neuron.circularpad2d.boundary.params import CircularPad2dBoundaryParams
from app.network.neuron.circularpad2d.boundary.options import CircularPad2dBoundaryOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.extension.circularpad.bounded import BoundedBoundaryStrategy
from app.gui.neuron.circularpad2d.boundary import UnboundedBoundaryStrategy


# View

class Boundary2dView(Enum):
    BOUNDED = ... #type: Boundary2dView
    UNBOUNDED = ... #type: Boundary2dView


# Main

class Boundary2dSwitcher(
    SwitcherProgram[
        Boundary2dView,
        NeuronBuilderDependencies,
        NeuronStrategyParams[CircularPad2dBoundaryParams, CircularPad2dBoundaryOptions]
    ]
):
    _bounded_strategy: BoundedBoundaryStrategy
    _unbounded_strategy: UnboundedBoundaryStrategy

    def __init__(self, key: Boundary2dView, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Boundary2dView, NeuronStrategy[CircularPad2dBoundaryParams, CircularPad2dBoundaryOptions]
    ]: ...

    @property
    def current_strategy(self) -> NeuronStrategy[CircularPad2dBoundaryParams, CircularPad2dBoundaryOptions]: ...
