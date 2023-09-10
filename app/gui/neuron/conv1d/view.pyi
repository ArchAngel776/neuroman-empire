from enum import Enum
from typing import Union

from lib.gui.element.switcher.program import SwitcherProgram

from app.network.neuron.conv1d.dimension.params import Conv1dDimensionParams
from app.network.neuron.conv1d.dimension.options import Conv1dDimensionOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.conv1d.dimension import SingleDimensionStrategy
from app.gui.neuron.conv1d.dimension.dependencies import SingleDimensionStrategyDependencies

# Type

Dimension1dDependencies = Union[SingleDimensionStrategyDependencies]


# View

class Dimension1dView(Enum):
    SINGLE = ... #type: Dimension1dView


# Main

class Dimension1dSwitcher(
    SwitcherProgram[
        Dimension1dView,
        Dimension1dDependencies,
        NeuronStrategyParams[Conv1dDimensionParams, Conv1dDimensionOptions]
    ]
):
    _single_strategy: SingleDimensionStrategy

    def __init__(self, key: Dimension1dView, dependencies: Dimension1dDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Dimension1dView,
        NeuronStrategy[Dimension1dDependencies, Conv1dDimensionParams, Conv1dDimensionOptions]
    ]: ...
