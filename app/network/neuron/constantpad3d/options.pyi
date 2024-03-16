from typing import Literal

from app.network.neuron.constantpad3d.boundary.options import ConstantPad3dBoundaryOptions

# Types

ConstantPad3dOptionsKeyof = Literal["bounded"]


# Main

class ConstantPad3dOptions(ConstantPad3dBoundaryOptions):
    bounded: bool
