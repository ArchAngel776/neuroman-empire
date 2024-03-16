from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ReflectionPad3dParams
from .options import ReflectionPad3dOptions


# Main

class ReflectionPadding3d(Neuron):
    @staticmethod
    def type():
        return NeuronType.REFLECTIONPAD3D

    @staticmethod
    def title():
        return "Reflection Padding 3D"

    @staticmethod
    def default_params():
        return ReflectionPad3dParams(
            padding=(0, 0, 0, 0, 0, 0)
        )

    @staticmethod
    def default_options():
        return ReflectionPad3dOptions(
            bounded=False
        )
