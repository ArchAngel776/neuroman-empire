from enum import Enum

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.neuron.zeropad3d.boundary.params import ZeroPad3dBoundaryParams
from app.network.neuron.zeropad3d.boundary.options import ZeroPad3dBoundaryOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.extension.zeropad.bounded import BoundedBoundaryStrategy
from app.gui.neuron.zeropad3d.boundary import UnboundedBoundaryStrategy


# View

class Boundary3dView(Enum):
    BOUNDED = ... #type: Boundary3dView
    UNBOUNDED = ... #type: Boundary3dView


# Main

class Boundary3dSwitcher(
    SwitcherProgram[
        Boundary3dView,
        NeuronBuilderDependencies,
        NeuronStrategyParams[ZeroPad3dBoundaryParams, ZeroPad3dBoundaryOptions]
    ]
):
    _bounded_strategy: BoundedBoundaryStrategy
    _unbounded_strategy: UnboundedBoundaryStrategy

    def __init__(self, key: Boundary3dView, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Boundary3dView, NeuronStrategy[ZeroPad3dBoundaryParams, ZeroPad3dBoundaryOptions]
    ]: ...

    @property
    def current_strategy(self) -> NeuronStrategy[ZeroPad3dBoundaryParams, ZeroPad3dBoundaryOptions]: ...
