from typing import Literal

from app.network.neuron.adaptiveavgpool3d.dimension.options import AdaptiveAvgPool3dDimensionOptions

# Types

AdaptiveAvgPool3dOptionsKeyof = Literal["cube"]


# Main

class AdaptiveAvgPool3dOptions(AdaptiveAvgPool3dDimensionOptions):
    cube: bool
