from typing import Literal

from app.network.neuron.avgpool1d.dimension.params import AvgPool1dDimensionParams

# Types

AvgPool1dParamsKeyof = Literal["ceil_mode", "count_include_pad"]


# Main

class AvgPool1dParams(AvgPool1dDimensionParams):
    ceil_mode: bool
    count_include_pad: bool
