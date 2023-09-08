from typing import Literal

from app.network.neuron.conv1d.dimension.params import Conv1dDimensionParams

# Types

Conv1dParamsKeyof = Literal["in_channels", "out_channels", "groups", "bias"]


# Main

class Conv1dParams(Conv1dDimensionParams):
    in_channels: int
    out_channels: int
    groups: int
    bias: bool
