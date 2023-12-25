from typing import Literal

from app.network.neuron.convtranspose2d.dimension.params import ConvTranspose2dDimensionParams

# Types

ConvTranspose2dParamsKeyof = Literal["in_channels", "out_channels", "groups", "bias"]


# Main

class ConvTranspose2dParams(ConvTranspose2dDimensionParams):
    in_channels: int
    out_channels: int
    groups: int
    bias: bool
