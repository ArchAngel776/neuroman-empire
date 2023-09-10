from typing import TypedDict, Callable, Any

from app.gui.neuron.conv2d import NeuronBuilderConvolution2dStrategy
from app.network.neuron.conv2d.params import Conv2dParams, Conv2dParamsKeyof
from app.network.neuron.conv2d.options import Conv2dOptions, Conv2dOptionsKeyof

# Types

InitParamCallback = Callable[
    [
        NeuronBuilderConvolution2dStrategy,
        Conv2dParamsKeyof | Callable[[Conv2dParams], Any]
    ],
    Any
]
InitOptionCallback = Callable[
    [
        NeuronBuilderConvolution2dStrategy,
        Conv2dOptionsKeyof | Callable[[Conv2dOptions], Any]
    ],
    Any
]


# Main

class Convolution2dStrategyDependencies(TypedDict):
    init_param: InitParamCallback
    init_option: InitOptionCallback
