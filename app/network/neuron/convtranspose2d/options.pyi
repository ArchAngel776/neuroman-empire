from typing import Literal

from app.network.neuron.convtranspose2d.dimension.options import ConvTranspose2dDimensionOptions

# Types

ConvTranspose2dOptionsKeyof = Literal["square"]


# Main

class ConvTranspose2dOptions(ConvTranspose2dDimensionOptions):
    square: bool
