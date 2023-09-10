from typing import TypedDict, Callable, Any

from app.gui.neuron.conv3d.dimension import TripleDimensionStrategy
from app.network.neuron.conv3d.dimension.params import Conv3dDimensionParams, Conv3dDimensionParamsKeyof
from app.network.neuron.conv3d.dimension.options import Conv3dDimensionOptions, Conv3dDimensionOptionsKeyof

# Types

InitParamCallback = Callable[
    [
        TripleDimensionStrategy,
        Conv3dDimensionParamsKeyof | Callable[[Conv3dDimensionParams], Any]
    ],
    Any
]
InitOptionCallback = Callable[
    [
        TripleDimensionStrategy,
        Conv3dDimensionOptionsKeyof | Callable[[Conv3dDimensionOptions], Any]
    ],
    Any
]


# Main

class TripleDimensionStrategyDependencies(TypedDict):
    init_param: InitParamCallback
    init_option: InitOptionCallback
