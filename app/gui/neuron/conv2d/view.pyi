from enum import Enum
from typing import Union

from lib.gui.element.switcher.program import SwitcherProgram

from app.network.neuron.conv2d.dimension.params import Conv2dDimensionParams
from app.network.neuron.conv2d.dimension.options import Conv2dDimensionOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.conv1d.dimension import SingleDimensionStrategy
from app.gui.neuron.conv2d.dimension import DoubleDimensionStrategy
from app.gui.neuron.conv1d.dimension.dependencies import SingleDimensionStrategyDependencies
from app.gui.neuron.conv2d.dimension.dependencies import DoubleDimensionStrategyDependencies

# Types

Dimension2dDependencies = Union[SingleDimensionStrategyDependencies, DoubleDimensionStrategyDependencies]


# View

class Dimension2dView(Enum):
    SINGLE = ... #type: Dimension2dView
    DOUBLE = ... #type: Dimension2dView


# Main

class Dimension2dSwitcher(
    SwitcherProgram[
        Dimension2dView,
        Dimension2dDependencies,
        NeuronStrategyParams[Conv2dDimensionParams, Conv2dDimensionOptions]
    ]
):
    _single_strategy: SingleDimensionStrategy
    _double_strategy: DoubleDimensionStrategy

    def __init__(self, key: Dimension2dView, dependencies: Dimension2dDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Dimension2dView,
        NeuronStrategy[Dimension2dDependencies, Conv2dDimensionParams, Conv2dDimensionOptions]
    ]: ...
