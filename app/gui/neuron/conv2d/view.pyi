from enum import Enum
from typing import Union

from lib.gui.element.switcher.program import SwitcherProgram
from lib.gui.element.switcher.strategy import SwitcherStrategy

from app.network.neuron.conv2d.dimension import Conv2dDimensionParams
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

class Dimension2dSwitcher(SwitcherProgram[Dimension2dView, Dimension2dDependencies, Conv2dDimensionParams]):
    _single_strategy: SingleDimensionStrategy
    _double_strategy: DoubleDimensionStrategy

    def __init__(self, key: Dimension2dView, dependencies: Dimension2dDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Dimension2dView,
        SwitcherStrategy[Dimension2dDependencies, Conv2dDimensionParams]
    ]: ...
