from typing import Literal

from app.network.neuron.reflectionpad1d.boundary.options import ReflectionPad1dBoundaryOptions

# Types

ReflectionPad1dOptionsKeyof = Literal["bounded"]


# Main

class ReflectionPad1dOptions(ReflectionPad1dBoundaryOptions):
    bounded: bool
