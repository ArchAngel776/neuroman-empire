from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import AvgPool1dParams
from .options import AvgPool1dOptions


# Main

class MaxPooling1d(Neuron[AvgPool1dParams, AvgPool1dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> AvgPool1dParams: ...

    @staticmethod
    def default_options() -> AvgPool1dOptions: ...
