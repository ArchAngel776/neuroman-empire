from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ZeroPad3dParams
from .options import ZeroPad3dOptions


# Main

class ZeroPadding3d(Neuron):
    @staticmethod
    def type():
        return NeuronType.ZEROPAD3D

    @staticmethod
    def title():
        return "Zero Padding 3D"

    @staticmethod
    def default_params():
        return ZeroPad3dParams(
            padding=(0, 0, 0, 0, 0, 0)
        )

    @staticmethod
    def default_options():
        return ZeroPad3dOptions(
            bounded=False
        )
