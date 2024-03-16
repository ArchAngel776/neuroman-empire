from typing import Literal

from app.network.neuron.reflectionpad3d.boundary.options import ReflectionPad3dBoundaryOptions

# Types

ReflectionPad3dOptionsKeyof = Literal["bounded"]


# Main

class ReflectionPad3dOptions(ReflectionPad3dBoundaryOptions):
    bounded: bool
