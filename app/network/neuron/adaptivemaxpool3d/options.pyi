from typing import Literal

from app.network.neuron.adaptivemaxpool3d.dimension.options import AdaptiveMaxPool3dDimensionOptions

# Types

AdaptiveMaxPool3dOptionsKeyof = Literal["cube"]


# Main

class AdaptiveMaxPool3dOptions(AdaptiveMaxPool3dDimensionOptions):
    cube: bool
