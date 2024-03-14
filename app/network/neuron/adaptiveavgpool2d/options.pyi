from typing import Literal

from app.network.neuron.adaptiveavgpool2d.dimension.options import AdaptiveAvgPool2dDimensionOptions

# Types

AdaptiveAvgPool2dOptionsKeyof = Literal["square"]


# Main

class AdaptiveAvgPool2dOptions(AdaptiveAvgPool2dDimensionOptions):
    square: bool
