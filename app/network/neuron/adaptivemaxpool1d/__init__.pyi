from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import AdaptiveMaxPool1dParams
from .options import AdaptiveMaxPool1dOptions


# Main

class AdaptiveMaxPooling1d(Neuron[AdaptiveMaxPool1dParams, AdaptiveMaxPool1dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> AdaptiveMaxPool1dParams: ...

    @staticmethod
    def default_options() -> AdaptiveMaxPool1dOptions: ...
