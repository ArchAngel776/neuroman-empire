from typing import TypedDict, Callable, Any

from app.gui.neuron.conv2d.dimension import DoubleDimensionStrategy
from app.network.neuron.conv2d.dimension.params import Conv2dDimensionParams, Conv2dDimensionParamsKeyof
from app.network.neuron.conv2d.dimension.options import Conv2dDimensionOptions, Conv2dDimensionOptionsKeyof

# Types

InitParamCallback = Callable[
    [
        DoubleDimensionStrategy,
        Conv2dDimensionParamsKeyof | Callable[[Conv2dDimensionParams], Any]
    ],
    Any
]
InitOptionCallback = Callable[
    [
        DoubleDimensionStrategy,
        Conv2dDimensionOptionsKeyof | Callable[[Conv2dDimensionOptions], Any]
    ],
    Any
]


# Main

class DoubleDimensionStrategyDependencies(TypedDict):
    init_param: InitParamCallback
    init_option: InitOptionCallback
