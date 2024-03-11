from typing import Literal

from app.network.neuron.fractionalmaxpool2d.dimension.options import FractionalMaxPool2dDimensionOptions

# Types

FractionalMaxPool2dDimensionOptionsKeyof = Literal["square"]


# Main

class FractionalMaxPool2dOptions(FractionalMaxPool2dDimensionOptions):
    square: bool
