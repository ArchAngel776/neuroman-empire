from typing import Literal

from app.network.neuron.constantpad2d.boundary.params import ConstantPad2dBoundaryParams

# Types

ConstantPad2dParamsKeyof = Literal["value"]


# Main

class ConstantPad2dParams(ConstantPad2dBoundaryParams):
    value: float
