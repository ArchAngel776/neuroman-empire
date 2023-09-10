from typing import TypedDict, Callable, Any

from app.gui.neuron.linear import NeuronBuilderLinearStrategy
from app.network.neuron.linear.params import LinearParams, LinearParamsKeyof
from app.network.neuron.linear.options import LinearOptions, LinearOptionsKeyof

# Types

InitParamCallback = Callable[
    [
        NeuronBuilderLinearStrategy,
        LinearParamsKeyof | Callable[[LinearParams], Any]
    ],
    Any
]
InitOptionCallback = Callable[
    [
        NeuronBuilderLinearStrategy,
        LinearOptionsKeyof | Callable[[LinearOptions], Any]
    ],
    Any
]


# Main

class LinearStrategyDependencies(TypedDict):
    init_param: InitParamCallback
    init_option: InitOptionCallback
