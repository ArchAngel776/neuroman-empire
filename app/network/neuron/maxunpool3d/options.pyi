from typing import Literal
from uuid import UUID

from app.network.neuron.maxunpool3d.dimension.options import MaxUnpool3dDimensionOptions

# Types

MaxPool1dOptionsKeyof = Literal["pooling", "cube"]


# Main

class MaxUnpool3dOptions(MaxUnpool3dDimensionOptions):
    pooling: UUID
    cube: bool
