from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ReflectionPad2dParams
from .options import ReflectionPad2dOptions


# Main

class ReflectionPadding2d(Neuron):
    @staticmethod
    def type():
        return NeuronType.REFLECTIONPAD2D

    @staticmethod
    def title():
        return "Reflection Padding 2D"

    @staticmethod
    def default_params():
        return ReflectionPad2dParams(
            padding=(0, 0, 0, 0)
        )

    @staticmethod
    def default_options():
        return ReflectionPad2dOptions(
            bounded=False
        )
