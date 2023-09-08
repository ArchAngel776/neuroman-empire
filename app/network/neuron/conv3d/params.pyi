from typing import Literal

from app.network.neuron.conv3d.dimension.params import Conv3dDimensionParams

# Types

Conv3dParamsKeyof = Literal["in_channels", "out_channels", "groups", "bias"]


# Main

class Conv3dParams(Conv3dDimensionParams):
    in_channels: int
    out_channels: int
    groups: int
    bias: bool
