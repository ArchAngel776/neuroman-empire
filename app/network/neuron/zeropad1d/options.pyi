from typing import Literal

from app.network.neuron.zeropad1d.boundary.options import ZeroPad1dBoundaryOptions

# Types

ZeroPad1dOptionsKeyof = Literal["bounded"]


# Main

class ZeroPad1dOptions(ZeroPad1dBoundaryOptions):
    bounded: bool
