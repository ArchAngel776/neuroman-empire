from typing import Literal

from app.network.neuron.circularpad3d.boundary.options import CircularPad3dBoundaryOptions

# Types

CircularPad3dOptionsKeyof = Literal["bounded"]


# Main

class CircularPad3dOptions(CircularPad3dBoundaryOptions):
    bounded: bool
