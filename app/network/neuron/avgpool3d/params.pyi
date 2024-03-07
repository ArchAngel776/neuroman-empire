from typing import Literal

from app.network.neuron.avgpool3d.dimension.params import AvgPool3dDimensionParams

# Types

AvgPool3dParamsKeyof = Literal["ceil_mode", "count_include_pad", "divisor_override"]


# Main

class AvgPool3dParams(AvgPool3dDimensionParams):
    ceil_mode: bool
    count_include_pad: bool
    divisor_override: int
