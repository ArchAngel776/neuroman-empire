from typing import Literal

from app.network.neuron.maxpool3d.dimension.options import MaxPool3dDimensionOptions

# Types

MaxPool3dOptionsKeyof = Literal["cube"]


# Main

class MaxPool3dOptions(MaxPool3dDimensionOptions):
    cube: bool
