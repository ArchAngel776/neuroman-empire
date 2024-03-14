from typing import Literal

from app.network.neuron.adaptivemaxpool2d.dimension.params import AdaptiveMaxPool2dDimensionParams

# Types

AdaptiveMaxPool2dParamsKeyof = Literal["return_indices"]


# Main

class AdaptiveMaxPool2dParams(AdaptiveMaxPool2dDimensionParams):
    return_indices: bool
