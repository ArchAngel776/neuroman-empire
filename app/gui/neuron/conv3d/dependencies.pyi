from typing import TypedDict, Callable, Any

from app.gui.neuron.conv3d import NeuronBuilderConvolution3dStrategy
from app.network.neuron.conv3d.params import Conv3dParams, Conv3dParamsKeyof
from app.network.neuron.conv3d.options import Conv3dOptions, Conv3dOptionsKeyof

# Types

InitParamCallback = Callable[
    [
        NeuronBuilderConvolution3dStrategy,
        Conv3dParamsKeyof | Callable[[Conv3dParams], Any]
    ],
    Any
]
InitOptionCallback = Callable[
    [
        NeuronBuilderConvolution3dStrategy,
        Conv3dOptionsKeyof | Callable[[Conv3dOptions], Any]
    ],
    Any
]


# Main

class Convolution3dStrategyDependencies(TypedDict):
    init_param: InitParamCallback
    init_option: InitOptionCallback
