from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import MaxPool1dParams
from .options import MaxPool1dOptions


# Main

class MaxPooling1d(Neuron[MaxPool1dParams, MaxPool1dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> MaxPool1dParams: ...

    @staticmethod
    def default_options() -> MaxPool1dOptions: ...
