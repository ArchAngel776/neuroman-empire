from typing import Literal

from app.network.neuron.constantpad1d.boundary.options import ConstantPad1dBoundaryOptions

# Types

ConstantPad1dOptionsKeyof = Literal["bounded"]


# Main

class ConstantPad1dOptions(ConstantPad1dBoundaryOptions):
    bounded: bool
