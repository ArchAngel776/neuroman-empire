from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ZeroPad2dParams
from .options import ZeroPad2dOptions


# Main

class ZeroPadding2d(Neuron[ZeroPad2dParams, ZeroPad2dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> ZeroPad2dParams: ...

    @staticmethod
    def default_options() -> ZeroPad2dOptions: ...
