from enum import Enum

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.neuron.circularpad1d.boundary.params import CircularPad1dBoundaryParams
from app.network.neuron.circularpad1d.boundary.options import CircularPad1dBoundaryOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.extension.circularpad.bounded import BoundedBoundaryStrategy
from app.gui.neuron.circularpad1d.boundary import UnboundedBoundaryStrategy


# View

class Boundary1dView(Enum):
    BOUNDED = ... #type: Boundary1dView
    UNBOUNDED = ... #type: Boundary1dView


# Main

class Boundary1dSwitcher(
    SwitcherProgram[
        Boundary1dView,
        NeuronBuilderDependencies,
        NeuronStrategyParams[CircularPad1dBoundaryParams, CircularPad1dBoundaryOptions]
    ]
):
    _bounded_strategy: BoundedBoundaryStrategy
    _unbounded_strategy: UnboundedBoundaryStrategy

    def __init__(self, key: Boundary1dView, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Boundary1dView, NeuronStrategy[CircularPad1dBoundaryParams, CircularPad1dBoundaryOptions]
    ]: ...

    @property
    def current_strategy(self) -> NeuronStrategy[CircularPad1dBoundaryParams, CircularPad1dBoundaryOptions]: ...
