from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import CircularPad1dParams
from .options import CircularPad1dOptions


# Main

class CircularPadding1d(Neuron):
    @staticmethod
    def type():
        return NeuronType.CIRCULARPAD1D

    @staticmethod
    def title():
        return "Circular Padding 1D"

    @staticmethod
    def default_params():
        return CircularPad1dParams(
            padding=(0, 0)
        )

    @staticmethod
    def default_options():
        return CircularPad1dOptions(
            bounded=False
        )
