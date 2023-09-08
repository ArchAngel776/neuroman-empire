from enum import Enum
from typing import Union

from lib.gui.element.switcher.program import SwitcherProgram
from lib.gui.element.switcher.strategy import SwitcherStrategy

from app.network.neuron.conv1d.dimension import Conv1dDimensionParams
from app.gui.neuron.conv1d.dimension import SingleDimensionStrategy
from app.gui.neuron.conv1d.dimension.dependencies import SingleDimensionStrategyDependencies

# Type

Dimension1dDependencies = Union[SingleDimensionStrategyDependencies]


# View

class Dimension1dView(Enum):
    SINGLE = ... #type: Dimension1dView


# Main

class Dimension1dSwitcher(SwitcherProgram[Dimension1dView, Dimension1dDependencies, Conv1dDimensionParams]):
    _single_strategy: SingleDimensionStrategy

    def __init__(self, key: Dimension1dView, dependencies: Dimension1dDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Dimension1dView,
        SwitcherStrategy[Dimension1dDependencies, Conv1dDimensionParams]
    ]: ...
