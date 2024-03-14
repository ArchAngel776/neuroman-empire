from enum import Enum

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.neuron.adaptiveavgpool3d.dimension.params import AdaptiveAvgPool3dDimensionParams
from app.network.neuron.adaptiveavgpool3d.dimension.options import AdaptiveAvgPool3dDimensionOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.adaptiveavgpool1d.dimension import SingleDimensionStrategy
from app.gui.neuron.adaptiveavgpool3d.dimension import TripleDimensionStrategy


# View

class Dimension3dView(Enum):
    SINGLE = ... #type: Dimension3dView
    TRIPLE = ... #type: Dimension3dView


# Main

class Dimension3dSwitcher(
    SwitcherProgram[
        Dimension3dView,
        NeuronBuilderDependencies,
        NeuronStrategyParams[AdaptiveAvgPool3dDimensionParams, AdaptiveAvgPool3dDimensionOptions]
    ]
):
    _single_strategy: SingleDimensionStrategy
    _triple_strategy: TripleDimensionStrategy

    def __init__(self, key: Dimension3dView, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Dimension3dView, NeuronStrategy[AdaptiveAvgPool3dDimensionParams, AdaptiveAvgPool3dDimensionOptions]
    ]: ...

    @property
    def current_strategy(self) -> NeuronStrategy[
        AdaptiveAvgPool3dDimensionParams, AdaptiveAvgPool3dDimensionOptions
    ]: ...
