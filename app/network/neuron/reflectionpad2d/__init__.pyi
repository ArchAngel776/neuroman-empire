from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ReflectionPad2dParams
from .options import ReflectionPad2dOptions


# Main

class ReflectionPadding2d(Neuron[ReflectionPad2dParams, ReflectionPad2dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> ReflectionPad2dParams: ...

    @staticmethod
    def default_options() -> ReflectionPad2dOptions: ...
