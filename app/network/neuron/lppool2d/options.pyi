from typing import Literal

from app.network.neuron.lppool2d.dimension.options import LPPool2dDimensionOptions

# Types

LPPool2dOptionsKeyof = Literal["square"]


# Main

class LPPool2dOptions(LPPool2dDimensionOptions):
    square: bool
