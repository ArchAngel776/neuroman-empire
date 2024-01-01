from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import MaxUnpool1dParams
from .options import MaxUnpool1dOptions


# Main

class MaxPooling1d(Neuron[MaxUnpool1dParams, MaxUnpool1dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> MaxUnpool1dParams: ...

    @staticmethod
    def default_options() -> MaxUnpool1dOptions: ...
