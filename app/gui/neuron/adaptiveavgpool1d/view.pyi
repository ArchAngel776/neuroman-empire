from enum import Enum

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.neuron.adaptiveavgpool1d.dimension.params import AdaptiveAvgPool1dDimensionParams
from app.network.neuron.adaptiveavgpool1d.dimension.options import AdaptiveAvgPool1dDimensionOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.adaptiveavgpool1d.dimension import SingleDimensionStrategy


# View

class Dimension1dView(Enum):
    SINGLE = ... #type: Dimension1dView


# Main

class Dimension1dSwitcher(
    SwitcherProgram[
        Dimension1dView,
        NeuronBuilderDependencies,
        NeuronStrategyParams[AdaptiveAvgPool1dDimensionParams, AdaptiveAvgPool1dDimensionOptions]
    ]
):
    _single_strategy: SingleDimensionStrategy

    def __init__(self, key: Dimension1dView, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Dimension1dView, NeuronStrategy[AdaptiveAvgPool1dDimensionParams, AdaptiveAvgPool1dDimensionOptions]
    ]: ...

    @property
    def current_strategy(self) -> NeuronStrategy[
        AdaptiveAvgPool1dDimensionParams, AdaptiveAvgPool1dDimensionOptions
    ]: ...
