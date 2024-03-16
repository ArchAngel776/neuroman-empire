from typing import Literal

from app.network.neuron.constantpad3d.boundary.params import ConstantPad3dBoundaryParams

# Types

ConstantPad3dParamsKeyof = Literal["value"]


# Main

class ConstantPad3dParams(ConstantPad3dBoundaryParams):
    value: float
