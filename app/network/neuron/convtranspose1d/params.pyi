from typing import Literal

from app.network.neuron.convtranspose1d.dimension.params import ConvTranspose1dDimensionParams

# Types

ConvTranspose1dParamsKeyof = Literal["in_channels", "out_channels", "groups", "bias"]


# Main

class ConvTranspose1dParams(ConvTranspose1dDimensionParams):
    in_channels: int
    out_channels: int
    groups: int
    bias: bool
