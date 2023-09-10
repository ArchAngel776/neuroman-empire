from typing import Literal

from app.network.neuron.conv3d.dimension.options import Conv3dDimensionOptions

# Types

Conv3dOptionsKeyof = Literal["cube"]


# Main

class Conv3dOptions(Conv3dDimensionOptions):
    cube: bool
