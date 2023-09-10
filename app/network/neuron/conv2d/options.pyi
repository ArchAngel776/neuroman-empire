from typing import Literal

from app.network.neuron.conv2d.dimension.options import Conv2dDimensionOptions

# Types

Conv2dOptionsKeyof = Literal["square"]


# Main

class Conv2dOptions(Conv2dDimensionOptions):
    square: bool
