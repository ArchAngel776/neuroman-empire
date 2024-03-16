from typing import Literal

from app.network.neuron.constantpad1d.boundary.params import ConstantPad1dBoundaryParams

# Types

ConstantPad1dParamsKeyof = Literal["value"]


# Main

class ConstantPad1dParams(ConstantPad1dBoundaryParams):
    value: float
