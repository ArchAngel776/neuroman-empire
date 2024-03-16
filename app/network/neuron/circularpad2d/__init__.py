from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import CircularPad2dParams
from .options import CircularPad2dOptions


# Main

class CircularPadding2d(Neuron):
    @staticmethod
    def type():
        return NeuronType.CIRCULARPAD2D

    @staticmethod
    def title():
        return "Circular Padding 2D"

    @staticmethod
    def default_params():
        return CircularPad2dParams(
            padding=(0, 0, 0, 0)
        )

    @staticmethod
    def default_options():
        return CircularPad2dOptions(
            bounded=False
        )
