from enum import Enum

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.neuron.adaptivemaxpool2d.dimension.params import AdaptiveMaxPool2dDimensionParams
from app.network.neuron.adaptivemaxpool2d.dimension.options import AdaptiveMaxPool2dDimensionOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.adaptivemaxpool1d.dimension import SingleDimensionStrategy
from app.gui.neuron.adaptivemaxpool2d.dimension import DoubleDimensionStrategy


# View

class Dimension2dView(Enum):
    SINGLE = ... #type: Dimension2dView
    DOUBLE = ... #type: Dimension2dView


# Main

class Dimension2dSwitcher(
    SwitcherProgram[
        Dimension2dView,
        NeuronBuilderDependencies,
        NeuronStrategyParams[AdaptiveMaxPool2dDimensionParams, AdaptiveMaxPool2dDimensionOptions]
    ]
):
    _single_strategy: SingleDimensionStrategy
    _double_strategy: DoubleDimensionStrategy

    def __init__(self, key: Dimension2dView, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def strategy(self) -> dict[
        Dimension2dView, NeuronStrategy[AdaptiveMaxPool2dDimensionParams, AdaptiveMaxPool2dDimensionOptions]
    ]: ...

    @property
    def current_strategy(self) -> NeuronStrategy[
        AdaptiveMaxPool2dDimensionParams, AdaptiveMaxPool2dDimensionOptions
    ]: ...
