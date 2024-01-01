from enum import Enum

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.neuron.convtranspose3d.dimension.params import ConvTranspose3dDimensionParams
from app.network.neuron.convtranspose3d.dimension.options import ConvTranspose3dDimensionOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.convtranspose1d.dimension import SingleDimensionStrategy
from app.gui.neuron.convtranspose3d.dimension import TripleDimensionStrategy


# View

class Dimension3dView(Enum):
    SINGLE = ... #type: Dimension3dView
    TRIPLE = ... #type: Dimension3dView


# Main

class Dimension3dSwitcher(
    SwitcherProgram[
        Dimension3dView,
        NeuronBuilderDependencies,
        NeuronStrategyParams[ConvTranspose3dDimensionParams, ConvTranspose3dDimensionOptions]
    ]
):
    _single_strategy: SingleDimensionStrategy
    _triple_strategy: TripleDimensionStrategy

    def __init__(self, key: Dimension3dView, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Dimension3dView,
        NeuronStrategy[ConvTranspose3dDimensionParams, ConvTranspose3dDimensionOptions]
    ]: ...

    @property
    def current_strategy(self) -> NeuronStrategy[ConvTranspose3dDimensionParams, ConvTranspose3dDimensionOptions]: ...
