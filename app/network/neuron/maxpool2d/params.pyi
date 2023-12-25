from typing import Literal

from app.network.neuron.maxpool2d.dimension.params import MaxPool2dDimensionParams

# Types

MaxPool2dParamsKeyof = Literal["ceil_mode", "return_indices"]


# Main

class MaxPool2dParams(MaxPool2dDimensionParams):
    ceil_mode: bool
    return_indices: bool
