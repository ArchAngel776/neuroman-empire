from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ConstantPad1dParams
from .options import ConstantPad1dOptions


# Main

class ConstantPadding1d(Neuron[ConstantPad1dParams, ConstantPad1dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> ConstantPad1dParams: ...

    @staticmethod
    def default_options() -> ConstantPad1dOptions: ...
