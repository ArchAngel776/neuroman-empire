from enum import Enum

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.neuron.lppool1d.dimension.params import LPPool1dDimensionParams
from app.network.neuron.lppool1d.dimension.options import LPPool1dDimensionOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.lppool1d.dimension import SingleDimensionStrategy


# View

class Dimension1dView(Enum):
    SINGLE = ... #type: Dimension1dView


# Main

class Dimension1dSwitcher(
    SwitcherProgram[
        Dimension1dView,
        NeuronBuilderDependencies,
        NeuronStrategyParams[LPPool1dDimensionParams, LPPool1dDimensionOptions]
    ]
):
    _single_strategy: SingleDimensionStrategy

    def __init__(self, key: Dimension1dView, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def strategy(self) -> dict[Dimension1dView, NeuronStrategy[LPPool1dDimensionParams, LPPool1dDimensionOptions]]: ...

    @property
    def current_strategy(self) -> NeuronStrategy[LPPool1dDimensionParams, LPPool1dDimensionOptions]: ...
