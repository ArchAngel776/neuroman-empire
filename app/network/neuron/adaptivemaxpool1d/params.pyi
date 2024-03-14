from typing import Literal

from app.network.neuron.adaptivemaxpool1d.dimension.params import AdaptiveMaxPool1dDimensionParams

# Types

AdaptiveMaxPool1dParamsKeyof = Literal["return_indices"]


# Main

class AdaptiveMaxPool1dParams(AdaptiveMaxPool1dDimensionParams):
    return_indices: bool
