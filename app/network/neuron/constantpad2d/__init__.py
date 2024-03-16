from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ConstantPad2dParams
from .options import ConstantPad2dOptions


# Main

class ConstantPadding2d(Neuron):
    @staticmethod
    def type():
        return NeuronType.CONSTANTPAD2D

    @staticmethod
    def title():
        return "Constant Padding 2D"

    @staticmethod
    def default_params():
        return ConstantPad2dParams(
            value=1.,
            padding=(0, 0, 0, 0)
        )

    @staticmethod
    def default_options():
        return ConstantPad2dOptions(
            bounded=False
        )
