from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import CircularPad3dParams
from .options import CircularPad3dOptions


# Main

class CircularPadding3d(Neuron):
    @staticmethod
    def type():
        return NeuronType.CIRCULARPAD3D

    @staticmethod
    def title():
        return "Circular Padding 3D"

    @staticmethod
    def default_params():
        return CircularPad3dParams(
            padding=(0, 0, 0, 0, 0, 0)
        )

    @staticmethod
    def default_options():
        return CircularPad3dOptions(
            bounded=False
        )
