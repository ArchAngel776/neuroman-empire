from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import CircularPad2dParams
from .options import CircularPad2dOptions


# Main

class CircularPadding2d(Neuron[CircularPad2dParams, CircularPad2dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> CircularPad2dParams: ...

    @staticmethod
    def default_options() -> CircularPad2dOptions: ...
