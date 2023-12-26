from enum import Enum

from lib.gui.element.switcher.program import SwitcherProgram

from app.network.neuron.maxpool3d.dimension.params import MaxPool3dDimensionParams
from app.network.neuron.maxpool3d.dimension.options import MaxPool3dDimensionOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.maxpool1d.dimension import SingleDimensionStrategy
from app.gui.neuron.maxpool3d.dimension import TripleDimensionStrategy


# View

class Dimension3dView(Enum):
    SINGLE = ... #type: Dimension3dView
    TRIPLE = ... #type: Dimension3dView


# Main

class Dimension3dSwitcher(
    SwitcherProgram[
        Dimension3dView,
        NeuronBuilderDependencies,
        NeuronStrategyParams[MaxPool3dDimensionParams, MaxPool3dDimensionOptions]
    ]
):
    _single_strategy: SingleDimensionStrategy
    _triple_strategy: TripleDimensionStrategy

    def __init__(self, key: Dimension3dView, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def strategy(self) -> dict[Dimension3dView, NeuronStrategy[MaxPool3dDimensionParams, MaxPool3dDimensionOptions]]: ...

    @property
    def current_strategy(self) -> NeuronStrategy[MaxPool3dDimensionParams, MaxPool3dDimensionOptions]: ...
