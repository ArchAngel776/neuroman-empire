from typing import Union

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.extension.fractionalmaxpool.single.options.output import Output
from app.network.extension.fractionalmaxpool.single.params.output.size import \
    FractionalMaxPoolSingleDimensionOutputSizeParams
from app.network.extension.fractionalmaxpool.single.options.output.size import \
    FractionalMaxPoolSingleDimensionOutputSizeOptions
from app.network.extension.fractionalmaxpool.single.params.output.ratio import \
    FractionalMaxPoolSingleDimensionOutputRatioParams
from app.network.extension.fractionalmaxpool.single.options.output.ratio import \
    FractionalMaxPoolSingleDimensionOutputRatioOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from .size import OutputSizeStrategy
from .ratio import OutputRatioStrategy

# Types

OutputParams = Union[
    NeuronStrategyParams[
        FractionalMaxPoolSingleDimensionOutputSizeParams,
        FractionalMaxPoolSingleDimensionOutputSizeOptions
    ],
    NeuronStrategyParams[
        FractionalMaxPoolSingleDimensionOutputRatioParams,
        FractionalMaxPoolSingleDimensionOutputRatioOptions
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
