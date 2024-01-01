from typing import Literal

from app.network.neuron.maxunpool1d.dimension.options import MaxUnpool1dDimensionOptions

# Types

MaxUnpool1dOptionsKeyof = Literal["indices"]


# Main

class MaxUnpool1dOptions(MaxUnpool1dDimensionOptions):
    indices: str
