from typing import Union

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.neuron.fractionalmaxpool2d.dimension.options.output import Output
from app.network.neuron.fractionalmaxpool2d.dimension.params.output.size import \
    FractionalMaxPool2dDimensionOutputSizeParams
from app.network.neuron.fractionalmaxpool2d.dimension.params.output.ratio import \
    FractionalMaxPool2dDimensionOutputRatioParams
from app.network.neuron.fractionalmaxpool2d.dimension.options.output.size import \
    FractionalMaxPool2dDimensionOutputSizeOptions
from app.network.neuron.fractionalmaxpool2d.dimension.options.output.ratio import \
    FractionalMaxPool2dDimensionOutputRatioOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from .size import OutputSizeStrategy
from .ratio import OutputRatioStrategy

# Types

OutputParams = Union[
    NeuronStrategyParams[
        FractionalMaxPool2dDimensionOutputSizeParams,
        FractionalMaxPool2dDimensionOutputSizeOptions
    ],
    NeuronStrategyParams[
        FractionalMaxPool2dDimensionOutputRatioParams,
        FractionalMaxPool2dDimensionOutputRatioOptions
    ]
]


# Main

class OutputSwitcher(SwitcherProgram[Output, NeuronBuilderDependencies, OutputParams]):
    _size_strategy: OutputSizeStrategy
    _ratio_strategy: OutputRatioStrategy

    def __init__(self, key: Output, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def strategy(self) -> dict[Output, Union[OutputSizeStrategy, OutputRatioStrategy]]: ...

    @property
    def current_strategy(self) -> Union[OutputSizeStrategy, OutputRatioStrategy]: ...
