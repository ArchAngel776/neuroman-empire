from typing import Literal

from app.network.neuron.fractionalmaxpool3d.dimension.params import FractionalMaxPool3dDimensionParams

# Types

FractionalMaxPool3dParamsKeyof = Literal["return_indices"]


# Main

class FractionalMaxPool3dParams(FractionalMaxPool3dDimensionParams):
    return_indices: bool
