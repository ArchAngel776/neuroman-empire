from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ZeroPad2dParams
from .options import ZeroPad2dOptions


# Main

class ZeroPadding2d(Neuron):
    @staticmethod
    def type():
        return NeuronType.ZEROPAD2D

    @staticmethod
    def title():
        return "Zero Padding 2D"

    @staticmethod
    def default_params():
        return ZeroPad2dParams(
            padding=(0, 0, 0, 0)
        )

    @staticmethod
    def default_options():
        return ZeroPad2dOptions(
            bounded=False
        )
