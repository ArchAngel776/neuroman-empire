from typing import Literal

from app.network.neuron.convtranspose3d.dimension.params import ConvTranspose3dDimensionParams

# Types

ConvTranspose3dParamsKeyof = Literal["in_channels", "out_channels", "groups", "bias"]


# Main

class ConvTranspose3dParams(ConvTranspose3dDimensionParams):
    in_channels: int
    out_channels: int
    groups: int
    bias: bool
