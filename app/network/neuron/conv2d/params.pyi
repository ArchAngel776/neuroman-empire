from typing import Literal

from app.network.neuron.conv2d.dimension.params import Conv2dDimensionParams

# Types

Conv2dParamsKeyof = Literal["in_channels", "out_channels", "groups", "bias"]


# Main

class Conv2dParams(Conv2dDimensionParams):
    in_channels: int
    out_channels: int
    groups: int
    bias: bool
