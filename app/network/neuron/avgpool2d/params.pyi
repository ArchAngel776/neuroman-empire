from typing import Literal

from app.network.neuron.avgpool2d.dimension.params import AvgPool2dDimensionParams

# Types

AvgPool2dParamsKeyof = Literal["ceil_mode", "count_include_pad", "divisor_override"]


# Main

class AvgPool2dParams(AvgPool2dDimensionParams):
    ceil_mode: bool
    count_include_pad: bool
    divisor_override: int
