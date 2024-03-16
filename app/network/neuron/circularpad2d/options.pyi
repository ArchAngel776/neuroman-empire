from typing import Literal

from app.network.neuron.circularpad2d.boundary.options import CircularPad2dBoundaryOptions

# Types

CircularPad2dOptionsKeyof = Literal["bounded"]


# Main

class CircularPad2dOptions(CircularPad2dBoundaryOptions):
    bounded: bool
