from typing import Literal

from app.network.neuron.lppool2d.dimension.params import LPPool2dDimensionParams

# Types

LPPool2dParamsKeyof = Literal["power", "ceil_mode"]


# Main

class LPPool2dParams(LPPool2dDimensionParams):
    power: int
    ceil_mode: bool
