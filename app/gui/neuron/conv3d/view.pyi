from enum import Enum
from typing import Union

from lib.gui.element.switcher.program import SwitcherProgram
from lib.gui.element.switcher.strategy import SwitcherStrategy

from app.network.neuron.conv3d.dimension import Conv3dDimensionParams
from app.gui.neuron.conv1d.dimension import SingleDimensionStrategy
from app.gui.neuron.conv3d.dimension import TripleDimensionStrategy
from app.gui.neuron.conv1d.dimension.dependencies import SingleDimensionStrategyDependencies
from app.gui.neuron.conv3d.dimension.dependencies import TripleDimensionStrategyDependencies

# Types

Dimension3dDependencies = Union[SingleDimensionStrategyDependencies, TripleDimensionStrategyDependencies]


# View

class Dimension3dView(Enum):
    SINGLE = ... #type: Dimension3dView
    TRIPLE = ... #type: Dimension3dView


# Main

class Dimension3dSwitcher(SwitcherProgram[Dimension3dView, Dimension3dDependencies, Conv3dDimensionParams]):
    _single_strategy: SingleDimensionStrategy
    _triple_strategy: TripleDimensionStrategy

    def __init__(self, key: Dimension3dView, dependencies: Dimension3dDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Dimension3dView,
        SwitcherStrategy[Dimension3dDependencies, Conv3dDimensionParams]
    ]: ...
