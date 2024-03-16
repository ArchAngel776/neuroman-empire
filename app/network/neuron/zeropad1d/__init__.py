from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ZeroPad1dParams
from .options import ZeroPad1dOptions


# Main

class ZeroPadding1d(Neuron):
    @staticmethod
    def type():
        return NeuronType.ZEROPAD1D

    @staticmethod
    def title():
        return "Zero Padding 1D"

    @staticmethod
    def default_params():
        return ZeroPad1dParams(
            padding=(0, 0)
        )

    @staticmethod
    def default_options():
        return ZeroPad1dOptions(
            bounded=False
        )
