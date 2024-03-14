from typing import Literal

from app.network.neuron.lppool1d.dimension.params import LPPool1dDimensionParams

# Types

LPPool1dParamsKeyof = Literal["power", "ceil_mode"]


# Main

class LPPool1dParams(LPPool1dDimensionParams):
    power: int
    ceil_mode: bool
