from typing import Literal

from app.network.neuron.maxpool3d.dimension.params import MaxPool3dDimensionParams

# Types

MaxPool3dParamsKeyof = Literal["ceil_mode", "return_indices"]


# Main

class MaxPool3dParams(MaxPool3dDimensionParams):
    ceil_mode: bool
    return_indices: bool
