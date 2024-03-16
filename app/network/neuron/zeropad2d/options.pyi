from typing import Literal

from app.network.neuron.zeropad2d.boundary.options import ZeroPad2dBoundaryOptions

# Types

ZeroPad2dOptionsKeyof = Literal["bounded"]


# Main

class ZeroPad2dOptions(ZeroPad2dBoundaryOptions):
    bounded: bool
