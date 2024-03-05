from typing import Literal
from uuid import UUID

from app.network.neuron.maxunpool1d.dimension.options import MaxUnpool1dDimensionOptions

# Types

MaxPool1dOptionsKeyof = Literal["pooling"]


# Main

class MaxUnpool1dOptions(MaxUnpool1dDimensionOptions):
    pooling: UUID
