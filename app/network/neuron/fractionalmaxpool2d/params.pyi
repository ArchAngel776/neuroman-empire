from typing import Literal

from app.network.neuron.fractionalmaxpool2d.dimension.params import FractionalMaxPool2dDimensionParams

# Types

FractionalMaxPool2dParamsKeyof = Literal["return_indices"]


# Main

class FractionalMaxPool2dParams(FractionalMaxPool2dDimensionParams):
    return_indices: bool
