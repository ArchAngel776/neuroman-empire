from enum import Enum
from typing import Union

from lib.gui.element.switcher.program import SwitcherProgram

from app.network.neuron.conv3d.dimension.params import Conv3dDimensionParams
from app.network.neuron.conv3d.dimension.options import Conv3dDimensionOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
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

class Dimension3dSwitcher(
    SwitcherProgram[
        Dimension3dView,
        Dimension3dDependencies,
        NeuronStrategyParams[Conv3dDimensionParams, Conv3dDimensionOptions]
    ]
):
    _single_strategy: SingleDimensionStrategy
    _triple_strategy: TripleDimensionStrategy

    def __init__(self, key: Dimension3dView, dependencies: Dimension3dDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Dimension3dView,
        NeuronStrategy[Dimension3dDependencies, Conv3dDimensionParams, Conv3dDimensionOptions]
    ]: ...
