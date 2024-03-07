from typing import Literal

from app.network.neuron.avgpool3d.dimension.options import AvgPool3dDimensionOptions

# Types

AvgPool3dOptionsKeyof = Literal["cube", "divisor_enabled"]


# Main

class AvgPool3dOptions(AvgPool3dDimensionOptions):
    cube: bool
    divisor_enabled: bool
