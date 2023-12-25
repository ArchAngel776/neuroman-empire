from typing import Literal

from app.network.neuron.convtranspose3d.dimension.options import ConvTranspose3dDimensionOptions

# Types

ConvTranspose3dOptionsKeyof = Literal["cube"]


# Main

class ConvTranspose3dOptions(ConvTranspose3dDimensionOptions):
    cube: bool
