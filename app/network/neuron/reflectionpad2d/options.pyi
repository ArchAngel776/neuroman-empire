from typing import Literal

from app.network.neuron.reflectionpad2d.boundary.options import ReflectionPad2dBoundaryOptions

# Types

ReflectionPad2dOptionsKeyof = Literal["bounded"]


# Main

class ReflectionPad2dOptions(ReflectionPad2dBoundaryOptions):
    bounded: bool
