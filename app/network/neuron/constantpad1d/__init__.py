from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ConstantPad1dParams
from .options import ConstantPad1dOptions


# Main

class ConstantPadding1d(Neuron):
    @staticmethod
    def type():
        return NeuronType.CONSTANTPAD1D

    @staticmethod
    def title():
        return "Constant Padding 1D"

    @staticmethod
    def default_params():
        return ConstantPad1dParams(
            value=1.,
            padding=(0, 0)
        )

    @staticmethod
    def default_options():
        return ConstantPad1dOptions(
            bounded=False
        )
