from typing import Literal

from app.network.neuron.maxpool1d.dimension.params import MaxPool1dDimensionParams

# Types

MaxPool1dParamsKeyof = Literal["ceil_mode", "return_indices"]


# Main

class MaxPool1dParams(MaxPool1dDimensionParams):
    ceil_mode: bool
    return_indices: bool
