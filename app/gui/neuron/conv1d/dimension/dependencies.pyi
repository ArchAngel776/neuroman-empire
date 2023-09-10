from typing import TypedDict, Callable, Any

from app.network.neuron.conv1d.dimension.params import Conv1dDimensionParams, Conv1dDimensionParamsKeyof
from app.network.neuron.conv1d.dimension.options import Conv1dDimensionOptions, Conv1dDimensionOptionsKeyof
from app.gui.neuron.conv1d.dimension import SingleDimensionStrategy

# Types

InitParamCallback = Callable[
    [
        SingleDimensionStrategy,
        Conv1dDimensionParamsKeyof | Callable[[Conv1dDimensionParams], Any]
    ],
    Any
]
InitOptionCallback = Callable[
    [
        SingleDimensionStrategy,
        Conv1dDimensionOptionsKeyof | Callable[[Conv1dDimensionOptions], Any]
    ],
    Any
]


# Main

class SingleDimensionStrategyDependencies(TypedDict):
    init_param: InitParamCallback
    init_option: InitOptionCallback
