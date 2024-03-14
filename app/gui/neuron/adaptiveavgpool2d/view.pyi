from enum import Enum

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.neuron.adaptiveavgpool2d.dimension.params import AdaptiveAvgPool2dDimensionParams
from app.network.neuron.adaptiveavgpool2d.dimension.options import AdaptiveAvgPool2dDimensionOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.adaptiveavgpool1d.dimension import SingleDimensionStrategy
from app.gui.neuron.adaptiveavgpool2d.dimension import DoubleDimensionStrategy


# View

class Dimension2dView(Enum):
    SINGLE = ... #type: Dimension2dView
    DOUBLE = ... #type: Dimension2dView


# Main

class Dimension2dSwitcher(
    SwitcherProgram[
        Dimension2dView,
        NeuronBuilderDependencies,
        NeuronStrategyParams[AdaptiveAvgPool2dDimensionParams, AdaptiveAvgPool2dDimensionOptions]
    ]
):
    _single_strategy: SingleDimensionStrategy
    _double_strategy: DoubleDimensionStrategy

    def __init__(self, key: Dimension2dView, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Dimension2dView, NeuronStrategy[AdaptiveAvgPool2dDimensionParams, AdaptiveAvgPool2dDimensionOptions]
    ]: ...

    @property
    def current_strategy(self) -> NeuronStrategy[
        AdaptiveAvgPool2dDimensionParams, AdaptiveAvgPool2dDimensionOptions
    ]: ...
