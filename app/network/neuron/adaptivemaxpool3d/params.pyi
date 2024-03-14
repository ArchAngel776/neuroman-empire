from typing import Literal

from app.network.neuron.adaptivemaxpool3d.dimension.params import AdaptiveMaxPool3dDimensionParams

# Types

AdaptiveMaxPool3dParamsKeyof = Literal["return_indices"]


# Main

class AdaptiveMaxPool3dParams(AdaptiveMaxPool3dDimensionParams):
    return_indices: bool
