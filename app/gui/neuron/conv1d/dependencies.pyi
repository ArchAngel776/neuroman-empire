from typing import TypedDict, Callable, Any

from app.gui.neuron.conv1d import NeuronBuilderConvolution1dStrategy
from app.network.neuron.conv1d.params import Conv1dParams, Conv1dParamsKeyof
from app.network.neuron.conv1d.options import Conv1dOptions, Conv1dOptionsKeyof


# Types

InitParamCallback = Callable[
    [
        NeuronBuilderConvolution1dStrategy,
        Conv1dParamsKeyof | Callable[[Conv1dParams], Any]
    ],
    Any
]
InitOptionCallback = Callable[
    [
        NeuronBuilderConvolution1dStrategy,
        Conv1dOptionsKeyof | Callable[[Conv1dOptions], Any]
    ],
    Any
]


# Main

class Convolution1dStrategyDependencies(TypedDict):
    init_param: InitParamCallback
    init_option: InitOptionCallback
