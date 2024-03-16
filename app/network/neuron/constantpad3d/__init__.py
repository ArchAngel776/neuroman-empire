from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ConstantPad3dParams
from .options import ConstantPad3dOptions


# Main

class ConstantPadding3d(Neuron):
    @staticmethod
    def type():
        return NeuronType.CONSTANTPAD3D

    @staticmethod
    def title():
        return "Constant Padding 3D"

    @staticmethod
    def default_params():
        return ConstantPad3dParams(
            value=1.,
            padding=(0, 0, 0, 0, 0, 0)
        )

    @staticmethod
    def default_options():
        return ConstantPad3dOptions(
            bounded=False
        )
