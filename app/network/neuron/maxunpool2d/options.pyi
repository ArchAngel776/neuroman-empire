from typing import Literal
from uuid import UUID

from app.network.neuron.maxunpool2d.dimension.options import MaxUnpool2dDimensionOptions

# Types

MaxPool2dOptionsKeyof = Literal["pooling", "square"]


# Main

class MaxUnpool2dOptions(MaxUnpool2dDimensionOptions):
    pooling: UUID
    square: bool
