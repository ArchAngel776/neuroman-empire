from typing import Literal

from app.network.neuron.circularpad1d.boundary.options import CircularPad1dBoundaryOptions

# Types

CircularPad1dOptionsKeyof = Literal["bounded"]


# Main

class CircularPad1dOptions(CircularPad1dBoundaryOptions):
    bounded: bool
