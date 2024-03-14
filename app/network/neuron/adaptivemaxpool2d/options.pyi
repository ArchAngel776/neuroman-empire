from typing import Literal

from app.network.neuron.adaptivemaxpool2d.dimension.options import AdaptiveMaxPool2dDimensionOptions

# Types

AdaptiveMaxPool2dOptionsKeyof = Literal["square"]


# Main

class AdaptiveMaxPool2dOptions(AdaptiveMaxPool2dDimensionOptions):
    square: bool
