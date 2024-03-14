from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import AdaptiveAvgPool1dParams
from .options import AdaptiveAvgPool1dOptions


# Main

class AdaptiveAveragePooling1d(Neuron[AdaptiveAvgPool1dParams, AdaptiveAvgPool1dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> AdaptiveAvgPool1dParams: ...

    @staticmethod
    def default_options() -> AdaptiveAvgPool1dOptions: ...
