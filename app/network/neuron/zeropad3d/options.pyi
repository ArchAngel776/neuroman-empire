from typing import Literal

from app.network.neuron.zeropad3d.boundary.options import ZeroPad3dBoundaryOptions

# Types

ZeroPad3dOptionsKeyof = Literal["bounded"]


# Main

class ZeroPad3dOptions(ZeroPad3dBoundaryOptions):
    bounded: bool
