from typing import Literal

from app.network.neuron.constantpad2d.boundary.options import ConstantPad2dBoundaryOptions

# Types

ConstantPad2dOptionsKeyof = Literal["bounded"]


# Main

class ConstantPad2dOptions(ConstantPad2dBoundaryOptions):
    bounded: bool
