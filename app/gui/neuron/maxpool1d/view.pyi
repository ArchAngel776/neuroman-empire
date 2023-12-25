from enum import Enum

from lib.gui.element.switcher.program import SwitcherProgram

from app.network.neuron.maxpool1d.dimension.params import MaxPool1dDimensionParams
from app.network.neuron.maxpool1d.dimension.options import MaxPool1dDimensionOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.maxpool1d.dimension import SingleDimensionStrategy


# View

class Dimension1dView(Enum):
    SINGLE = ... #type: Dimension1dView


# Main

class Dimension1dSwitcher(
    SwitcherProgram[Dimension1dView, {}, NeuronStrategyParams[MaxPool1dDimensionParams, MaxPool1dDimensionOptions]]
):
    _single_strategy: SingleDimensionStrategy

    def __init__(self, key: Dimension1dView) -> None: ...

    @property
    def strategy(self) -> dict[Dimension1dView, NeuronStrategy[MaxPool1dDimensionParams, MaxPool1dDimensionOptions]]: ...

    @property
    def current_strategy(self) -> NeuronStrategy[MaxPool1dDimensionParams, MaxPool1dDimensionOptions]: ...
