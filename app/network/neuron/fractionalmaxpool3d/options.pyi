from typing import Literal

from app.network.neuron.fractionalmaxpool3d.dimension.options import FractionalMaxPool3dDimensionOptions

# Types

FractionalMaxPool3dDimensionOptionsKeyof = Literal["cube"]


# Main

class FractionalMaxPool3dOptions(FractionalMaxPool3dDimensionOptions):
    cube: bool
