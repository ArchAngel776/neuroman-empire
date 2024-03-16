from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ConstantPad2dParams
from .options import ConstantPad2dOptions


# Main

class ConstantPadding2d(Neuron[ConstantPad2dParams, ConstantPad2dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> ConstantPad2dParams: ...

    @staticmethod
    def default_options() -> ConstantPad2dOptions: ...
