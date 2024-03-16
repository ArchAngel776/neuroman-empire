from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ReflectionPad1dParams
from .options import ReflectionPad1dOptions


# Main

class ReflectionPadding1d(Neuron):
    @staticmethod
    def type():
        return NeuronType.REFLECTIONPAD1D

    @staticmethod
    def title():
        return "Reflection Padding 1D"

    @staticmethod
    def default_params():
        return ReflectionPad1dParams(
            padding=(0, 0)
        )

    @staticmethod
    def default_options():
        return ReflectionPad1dOptions(
            bounded=False
        )
