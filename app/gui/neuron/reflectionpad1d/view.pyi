from enum import Enum

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.neuron.reflectionpad1d.boundary.params import ReflectionPad1dBoundaryParams
from app.network.neuron.reflectionpad1d.boundary.options import ReflectionPad1dBoundaryOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.extension.reflectionpad.bounded import BoundedBoundaryStrategy
from app.gui.neuron.reflectionpad1d.boundary import UnboundedBoundaryStrategy


# View

class Boundary1dView(Enum):
    BOUNDED = ... #type: Boundary1dView
    UNBOUNDED = ... #type: Boundary1dView


# Main

class Boundary1dSwitcher(
    SwitcherProgram[
        Boundary1dView,
        NeuronBuilderDependencies,
        NeuronStrategyParams[ReflectionPad1dBoundaryParams, ReflectionPad1dBoundaryOptions]
    ]
):
    _bounded_strategy: BoundedBoundaryStrategy
    _unbounded_strategy: UnboundedBoundaryStrategy

    def __init__(self, key: Boundary1dView, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Boundary1dView, NeuronStrategy[ReflectionPad1dBoundaryParams, ReflectionPad1dBoundaryOptions]
    ]: ...

    @property
    def current_strategy(self) -> NeuronStrategy[ReflectionPad1dBoundaryParams, ReflectionPad1dBoundaryOptions]: ...
