from typing import Literal

from app.network.neuron.maxpool2d.dimension.options import MaxPool2dDimensionOptions

# Types

MaxPool2dOptionsKeyof = Literal["square"]


# Main

class MaxPool2dOptions(MaxPool2dDimensionOptions):
    square: bool
