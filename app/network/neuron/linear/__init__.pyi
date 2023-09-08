from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import LinearParams
from .options import LinearOptions


# Main

class Linear(Neuron[LinearParams, LinearOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> LinearParams: ...

    @staticmethod
    def default_options() -> LinearOptions: ...
