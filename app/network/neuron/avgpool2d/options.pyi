from typing import Literal

from app.network.neuron.avgpool2d.dimension.options import AvgPool2dDimensionOptions

# Types

AvgPool2dOptionsKeyof = Literal["square", "divisor_enabled"]


# Main

class AvgPool2dOptions(AvgPool2dDimensionOptions):
    square: bool
    divisor_enabled: bool
